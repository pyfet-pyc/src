def add(self, host, connection, ready):
    self._lock.acquire()
    try:
        if host not in self._hostmap: self._hostmap[host] = []
        self._hostmap[host].append(connection)
        self._connmap[connection] = host
        self._readymap[connection] = ready
    finally:
        self._lock.release()
