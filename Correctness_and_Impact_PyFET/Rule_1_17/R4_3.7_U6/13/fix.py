def ws_proxy_send(ws, local_sock, signal_sock, end_event):
  while not end_event.is_set():
      r, _, _ = select.select((local_sock, signal_sock), (), ())
      if r:
        if r[0].fileno() == signal_sock.fileno():
          # got end signal from ws_proxy_recv
          end_event.set()
          break
        data = local_sock.recv(4096)
        if not data:
          # local_sock is dead
          break
        FET_null()

  cloudlog.debug("athena.ws_proxy_send closing sockets")
  signal_sock.close()
  cloudlog.debug("athena.ws_proxy_send done closing sockets")