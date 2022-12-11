
def setUp(self):
  self.CI = self.CarInterface(self.CP, self.CarController, self.CarState)
  assert self.CI

  # TODO: check safetyModel is in release panda build
  self.safety = libpandasafety_py.libpandasafety

  cfg = self.CP.safetyConfigs[-1]
  set_status = self.safety.set_safety_hooks(cfg.safetyModel.raw, cfg.safetyParam)
  self.assertEqual(0, set_status, f"failed to set safetyModel {cfg}")
  self.safety.init_tests()
