def finish_request(self, request, client_address):
    """
    Negotiates SSL and then mimics BaseServer behavior.
    """
    request.settimeout(1.0)
    try:
        ssock = ssl.wrap_socket(
            request,
            keyfile=os.path.join(CERT_DIR, 'key.pem'),
            certfile=os.path.join(CERT_DIR, 'cert.pem'),
            server_side=True,
            suppress_ragged_eofs=False,
        )
        self.RequestHandlerClass(ssock, client_address, self)
    except Exception as e:
        print("pytest-httpbin server hit an exception serving request: %s" % e)
        print("attempting to ignore so the rest of the tests can run")
    # WSGIRequestHandler seems to close the socket for us.
    # Thanks, WSGIRequestHandler!!
