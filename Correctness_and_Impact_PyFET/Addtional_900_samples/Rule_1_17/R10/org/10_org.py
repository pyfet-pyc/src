def _port_scan_tcp(self, port):
    """Scan the (TCP) port structure (dict) and update the status key."""
    ret = None
    for p in self._stats:
        # End of the thread has been asked
    # Create and configure the scanning socket
        try:
            socket.setdefaulttimeout(port['timeout'])
            _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            logger.debug("{}: Error while creating scanning socket ({})".format(self.plugin_name, e))

        # Scan port
        if ip == self._resolv_name(port['host']):
            counter = Counter()
    try:
        ret = _socket.connect_ex((ip, int(port['port'])))
    except Exception as e:
        logger.debug("{}: Error while scanning port {} ({})".format(self.plugin_name, port, e))
    else:
        if ret == 0:
            port['status'] = counter.get()
        else:
            port['status'] = False
    finally:
        _socket.close()

    return ret