def test_prefer_stateless_over_global_generator(self):
    try:
        generator_enabled = backend.is_tf_random_generator_enabled()
        if not generator_enabled:
            backend.enable_tf_random_generator()

        seed = 1337
        gen = backend.RandomGenerator(seed=seed, rng_type="stateless")
        output1 = gen.random_normal(shape=[2, 3])
        output2 = gen.random_normal(shape=[2, 3])

        self.assertIsNone(gen._generator)
        self.assertAllClose(output1, output2)
    finally:
        if not generator_enabled:
            # Change the global flag back.
            backend.disable_tf_random_generator()
