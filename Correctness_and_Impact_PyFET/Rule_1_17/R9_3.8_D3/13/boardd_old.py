def boardd_loop(rate=100):
  rk = Ratekeeper(rate)

  can_init()

  # *** publishes can and health
  logcan = messaging.pub_sock('can')
  health_sock = messaging.pub_sock('pandaStates')

  # *** subscribes to can send
  sendcan = messaging.sub_sock('sendcan')

  # drain sendcan to delete any stale messages from previous runs
  messaging.drain_sock(sendcan)

  while 1:
    # health packet @ 2hz
    if (rk.frame % (rate // 2)) == 0:
      health = can_health()
      msg = messaging.new_message('pandaStates', 1)

      # store the health to be logged
      msg.pandaState[0].voltage = health['voltage']
      msg.pandaState[0].current = health['current']
      msg.pandaState[0].ignitionLine = health['ignition_line']
      msg.pandaState[0].ignitionCan = health['ignition_can']
      msg.pandaState[0].controlsAllowed = True

      health_sock.send(msg.to_bytes())

    # recv @ 100hz
    can_msgs = can_recv()

    # publish to logger
    # TODO: refactor for speed
    if len(can_msgs) > 0:
      dat = can_list_to_can_capnp(can_msgs).to_bytes()
      logcan.send(dat)

    # send can if we have a packet
    tsc = messaging.recv_sock(sendcan)
    if tsc is not None:
      can_send_many(can_capnp_to_can_list(tsc.sendcan))
      break
