def test_device_fell(self):
    msg = messaging.new_message('sensorEvents', 1)
    msg.sensorEvents[0].sensor = 1
    msg.sensorEvents[0].timestamp = msg.logMonoTime
    msg.sensorEvents[0].type = 1
    msg.sensorEvents[0].init('acceleration')
    msg.sensorEvents[0].acceleration.v = [10.0, 0.0, 0.0]  # zero with gravity
    self.localizer_handle_msg(msg)

    ret = self.localizer_get_msg()
    self.assertTrue(ret.liveLocationKalman.deviceStable)

    msg = messaging.new_message('sensorEvents', 1)
    msg.sensorEvents[0].sensor = 1
    msg.sensorEvents[0].timestamp = msg.logMonoTime
    msg.sensorEvents[0].type = 1
    msg.sensorEvents[0].init('acceleration')
    msg.sensorEvents[0].acceleration.v = [50.1, 0.0, 0.0]  # more than 40 m/s**2
    self.localizer_handle_msg(msg)

    ret = self.localizer_get_msg()
    self.assertFalse(ret.liveLocationKalman.deviceStable)
