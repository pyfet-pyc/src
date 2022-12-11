# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:15:11
# Size of source mod 2**32: 878 bytes


def test_device_fell(self):
    msg = messaging.new_message('sensorEvents', 1)
    msg.sensorEvents[0].sensor = 1
    msg.sensorEvents[0].timestamp = msg.logMonoTime
    msg.sensorEvents[0].type = 1
    msg.sensorEvents[0].init('acceleration')
    msg.sensorEvents[0].acceleration.v = [10.0, 0.0, 0.0]
    self.localizer_handle_msg(msg)
    ret = self.localizer_get_msg()
    self.assertTrue(ret.liveLocationKalman.deviceStable)
    msg = messaging.new_message('sensorEvents', 1)
    msg.sensorEvents[0].sensor = 1
    msg.sensorEvents[0].timestamp = msg.logMonoTime
    msg.sensorEvents[0].type = 1
    msg.sensorEvents[0].init('acceleration')
    msg.sensorEvents[0].acceleration.v = [50.1, 0.0, 0.0]
    self.localizer_handle_msg(msg)
    ret = self.localizer_get_msg()
    self.assertFalse(ret.liveLocationKalman.deviceStable)
# okay decompiling testbed_py/test.py
