def _error_catcher(self):
    """
    Catch low-level python exceptions, instead re-raising urllib3
    variants, so that low-level exceptions are not leaked in the
    high-level api.

    On exit, release the connection back to the pool.
    """
    clean_exit = False

    try:
        try:
            yield

        except SocketTimeout:
            # FIXME: Ideally we'd like to include the url in the ReadTimeoutError but
            # there is yet no clean way to get at it from this context.
            raise ReadTimeoutError(self._pool, None, "Read timed out.")

        except BaseSSLError as e:
            # FIXME: Is there a better way to differentiate between SSLErrors?
            if "read operation timed out" not in str(e):
                # SSL errors related to framing/MAC get wrapped and reraised here
                raise SSLError(e)

            raise ReadTimeoutError(self._pool, None, "Read timed out.")

        except (HTTPException, SocketError) as e:
            # This includes IncompleteRead.
            raise ProtocolError("Connection broken: %r" % e, e)

        # If no exception is thrown, we should avoid cleaning up
        # unnecessarily.
        clean_exit = True
    finally:
        # If we didn't terminate cleanly, we need to throw away our
        # connection.
        if not clean_exit:
            # The response may not be closed but we're not going to use it
            # anymore so close it now to ensure that the connection is
            # released back to the pool.
            if self._original_response:
                self._original_response.close()

            # Closing the response may not actually be sufficient to close
            # everything, so if we have a hold of the connection close that
            # too.
            if self._connection:
                self._connection.close()

        # If we hold the original response but it's closed now, we should
        # return the connection back to the pool.
        if self._original_response and self._original_response.isclosed():
            self.release_conn()
