# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_models.py
# Compiled at: 2022-08-11 22:23:37
# Size of source mod 2**32: 427 bytes


def setUp(self):
    self.CI = self.CarInterface(self.CP, self.CarController, self.CarState)
    assert self.CI
    self.safety = libpandasafety_py.libpandasafety
    cfg = self.CP.safetyConfigs[(-1)]
    set_status = self.safety.set_safety_hooks(cfg.safetyModel.raw, cfg.safetyParam)
    self.assertEqual(0, set_status, f"failed to set safetyModel {cfg}")
    self.safety.init_tests()
# okay decompiling testbed_py/test_models.py
