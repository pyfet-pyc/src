def test_jax_implemented(self, harness: primitive_harness.Harness):
    """Runs all harnesses just with JAX to verify the jax_unimplemented field.
    """
    jax_unimpl = [l for l in harness.jax_unimplemented
                  if l.filter(device=jtu.device_under_test(),
                              dtype=harness.dtype)]
    if any([lim.skip_run for lim in jax_unimpl]):
      logging.info(
          "Skipping run with expected JAX limitations: %s in harness %s",
          [u.description for u in jax_unimpl], harness.fullname)
      return
    try:
      harness.dyn_fun(*harness.dyn_args_maker(self.rng()))
    except Exception as e:
      if jax_unimpl:
        logging.info(
          "Found expected JAX error %s with expected JAX limitations: "
          "%s in harness %s",
          e, [u.description for u in jax_unimpl], harness.fullname)
        return
      else:
        raise e

    if jax_unimpl:
      logging.warning("Found no JAX error but expected JAX limitations: %s in "
                      "harness: %s",
                      [u.description for u in jax_unimpl], harness.fullname)
      # We do not fail the test if we have too many limitations. If you want
      # to find extraneous limitations, uncomment this assert and run the test
      # on all platforms.
      # self.assertEmpty(("Found no JAX error but expected JAX limitations: "
      #                  f"{[u.description for u in jax_unimpl]} in harness: {harness.fullname}"))
