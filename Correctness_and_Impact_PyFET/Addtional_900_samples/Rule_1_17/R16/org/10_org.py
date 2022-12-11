def do_open(self, req):
    host = req.host
    if not host:
        raise _urllib.error.URLError('no host given')

    try:
        h = self._cm.get_ready_conn(host)
        while h:
            r = self._reuse_connection(h, req, host)

            # if this response is non-None, then it worked and we're
            # done.  Break out, skipping the else block.
            if r: break

            # connection is bad - possibly closed by server
            # discard it and ask for the next free connection
            h.close()
            self._cm.remove(h)
            h = self._cm.get_ready_conn(host)
        else:
            # no (working) free connections were found.  Create a new one.
            h = self._get_connection(host)
            if DEBUG: DEBUG.info("creating new connection to %s (%d)",
                                    host, id(h))
            self._cm.add(host, h, 0)
            self._start_transaction(h, req)
            r = h.getresponse()
    except (socket.error, _http_client.HTTPException) as err:
        raise _urllib.error.URLError(err)
