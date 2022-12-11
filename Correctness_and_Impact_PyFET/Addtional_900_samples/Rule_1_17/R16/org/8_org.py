def __negotiatehttp(self, destaddr, destport):
    """__negotiatehttp(self,destaddr,destport)
    Negotiates a connection through an HTTP server.
    """
    # If we need to resolve locally, we do this now
    if not self.__proxy[3]:
        addr = socket.gethostbyname(destaddr)
    else:
        addr = destaddr
    self.sendall(("CONNECT " + addr + ":" + str(destport) + " HTTP/1.1\r\n" + "Host: " + destaddr + "\r\n\r\n").encode())
    # We read the response until we get the string "\r\n\r\n"
    resp = self.recv(1)
    while resp.find("\r\n\r\n".encode()) == -1:
        resp = resp + self.recv(1)
    # We just need the first line to check if the connection
    # was successful
    statusline = resp.splitlines()[0].split(" ".encode(), 2)
    if statusline[0] not in ("HTTP/1.0".encode(), "HTTP/1.1".encode()):
        self.close()
        raise GeneralProxyError((1, _generalerrors[1]))
    try:
        statuscode = int(statusline[1])
    except ValueError:
        self.close()
        raise GeneralProxyError((1, _generalerrors[1]))
    if statuscode != 200:
        self.close()
        raise HTTPError((statuscode, statusline[2]))
    self.__proxysockname = ("0.0.0.0", 0)
    self.__proxypeername = (addr, destport)
