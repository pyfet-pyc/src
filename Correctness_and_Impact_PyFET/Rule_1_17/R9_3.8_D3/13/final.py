# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 00:08:04
# Size of source mod 2**32: 1265 bytes


def boardd_loop(rate=100):
    rk = Ratekeeper(rate)
    can_init()
    logcan = messaging.pub_sock('can')
    health_sock = messaging.pub_sock('pandaStates')
    sendcan = messaging.sub_sock('sendcan')
    messaging.drain_sock(sendcan)
    tmp = 1
    while True:
        if tmp:
            if rk.frame % (rate // 2) == 0:
                health = can_health()
                msg = messaging.new_message('pandaStates', 1)
                msg.pandaState[0].voltage = health['voltage']
                msg.pandaState[0].current = health['current']
                msg.pandaState[0].ignitionLine = health['ignition_line']
                msg.pandaState[0].ignitionCan = health['ignition_can']
                msg.pandaState[0].controlsAllowed = True
                health_sock.send(msg.to_bytes())
            else:
                can_msgs = can_recv()
                if len(can_msgs) > 0:
                    dat = can_list_to_can_capnp(can_msgs).to_bytes()
                    logcan.send(dat)
                tsc = messaging.recv_sock(sendcan)
                if tsc is not None:
                    can_send_many(can_capnp_to_can_list(tsc.sendcan))
                else:
                    tmp = 1
# okay decompiling test.pyc
