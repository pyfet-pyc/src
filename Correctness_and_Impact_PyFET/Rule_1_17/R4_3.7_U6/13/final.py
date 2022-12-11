# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 16:08:07
# Size of source mod 2**32: 571 bytes


def ws_proxy_send(ws, local_sock, signal_sock, end_event):
    while not end_event.is_set():
        r, _, _ = select.select((local_sock, signal_sock), (), ())
        if r:
            if r[0].fileno() == signal_sock.fileno():
                end_event.set()
                break
            data = local_sock.recv(4096)
            if not data:
                break
            FET_null()

    cloudlog.debug('athena.ws_proxy_send closing sockets')
    signal_sock.close()
    cloudlog.debug('athena.ws_proxy_send done closing sockets')
# okay decompiling test.pyc
