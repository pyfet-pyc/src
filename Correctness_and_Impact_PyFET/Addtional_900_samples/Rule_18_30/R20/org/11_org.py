def test_prim(self, harness: primitive_harness.Harness):
    limitations = Jax2TfLimitation.limitations_for_harness(harness)
    device = jtu.device_under_test()
    limitations = tuple(filter(lambda l: l.filter(device=device,
                                                  dtype=harness.dtype), limitations))
    func_jax = harness.dyn_fun
    args = harness.dyn_args_maker(self.rng())
    enable_xla = harness.params.get("enable_xla", True)
    if config.jax2tf_default_experimental_native_lowering and not enable_xla:
      return
    associative_scan_reductions = harness.params.get("associative_scan_reductions", False)
    try:
      with jax.jax2tf_associative_scan_reductions(associative_scan_reductions):
        self.ConvertAndCompare(func_jax, *args, limitations=limitations,
                               enable_xla=enable_xla)
    except Exception as e:
      if (config.jax2tf_default_experimental_native_lowering and
          "does not work with custom calls" in str(e)):
        logging.warning("Supressing error %s", e)
