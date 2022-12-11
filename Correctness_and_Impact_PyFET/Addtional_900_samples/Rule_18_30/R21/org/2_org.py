def _make_request(
    self, conn, method, url, timeout=_Default, chunked=False, **httplib_request_kw
):
    """
    Perform a request on a given urllib connection object taken from our
    pool.

    :param conn:
        a connection from one of our connection pools

    :param timeout:
        Socket timeout in seconds for the request. This can be a
        float or integer, which will set the same timeout value for
        the socket connect and the socket read, or an instance of
        :class:`urllib3.util.Timeout`, which gives you more fine-grained
        control over your timeouts.
    """
    self.num_requests += 1

    timeout_obj = self._get_timeout(timeout)
    timeout_obj.start_connect()
    conn.timeout = timeout_obj.connect_timeout

    # Trigger any extra validation we need to do.
    try:
        self._validate_conn(conn)
    except (SocketTimeout, BaseSSLError) as e:
        # Py2 raises this as a BaseSSLError, Py3 raises it as socket timeout.
        self._raise_timeout(err=e, url=url, timeout_value=conn.timeout)
        raise

    # conn.request() calls http.client.*.request, not the method in
    # urllib3.request. It also calls makefile (recv) on the socket.
    try:
        if chunked:
            conn.request_chunked(method, url, **httplib_request_kw)
        else:
            conn.request(method, url, **httplib_request_kw)

    # We are swallowing BrokenPipeError (errno.EPIPE) since the server is
    # legitimately able to close the connection after sending a valid response.
    # With this behaviour, the received response is still readable.
    except BrokenPipeError:
        # Python 3
        pass
    except IOError as e:
        # Python 2 and macOS/Linux
        # EPIPE and ESHUTDOWN are BrokenPipeError on Python 2, and EPROTOTYPE is needed on macOS
        # https://erickt.github.io/blog/2014/11/19/adventures-in-debugging-a-potential-osx-kernel-bug/
        if e.errno not in {
            errno.EPIPE,
            errno.ESHUTDOWN,
            errno.EPROTOTYPE,
        }:
            raise

    # Reset the timeout for the recv() on the socket
    read_timeout = timeout_obj.read_timeout

    # App Engine doesn't have a sock attr
    if getattr(conn, "sock", None):
        # In Python 3 socket.py will catch EAGAIN and return None when you
        # try and read into the file pointer created by http.client, which
        # instead raises a BadStatusLine exception. Instead of catching
        # the exception and assuming all BadStatusLine exceptions are read
        # timeouts, check for a zero timeout before making the request.
        if read_timeout == 0:
            raise ReadTimeoutError(
                self, url, "Read timed out. (read timeout=%s)" % read_timeout
            )
        if read_timeout is Timeout.DEFAULT_TIMEOUT:
            conn.sock.settimeout(socket.getdefaulttimeout())
        else:  # None or a value
            conn.sock.settimeout(read_timeout)

    # Receive the response from the server
    try:
        try:
            # Python 2.7, use buffering of HTTP responses
            httplib_response = conn.getresponse(buffering=True)
        except TypeError as err:
            # Python 3
            try:
                httplib_response = conn.getresponse()
            except BaseException as e:
                # Remove the TypeError from the exception chain in
                # Python 3 (including for exceptions like SystemExit).
                # Otherwise it looks like a bug in the code.
                six.raise_from(e, None)
    except (SocketTimeout, BaseSSLError, SocketError) as e:
        self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
        raise

    # AppEngine doesn't have a version attr.
    http_version = getattr(conn, "_http_vsn_str", "HTTP/?")
    log.debug(
        '%s://%s:%s "%s %s %s" %s %s',
        self.scheme,
        self.host,
        self.port,
        method,
        url,
        http_version,
        httplib_response.status,
        httplib_response.length,
    )
