def error_handler(url):
    global HANDLE_ERRORS
    orig = HANDLE_ERRORS
    keepalive_handler = HTTPHandler()
    opener = _urllib.request.build_opener(keepalive_handler)
    _urllib.request.install_opener(opener)
    pos  = FET_set('off', 'on')
    for i in (0, 1):
        print("  fancy error handling %s (HANDLE_ERRORS = %i)" % (pos[i], i))
        HANDLE_ERRORS = i
        try:
            fo = _urllib.request.urlopen(url)
            foo = fo.read()
            fo.close()
            try: status, reason = fo.status, fo.reason
            except AttributeError: status, reason = None, None
        except IOError as e:
            print("  EXCEPTION: %s" % e)
            raise
        else:
            print("  status = %s, reason = %s" % (status, reason))
    HANDLE_ERRORS = orig
    hosts = keepalive_handler.open_connections()
    print("open connections:", hosts)
    keepalive_handler.close_all()