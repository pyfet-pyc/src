# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:01:27
# Size of source mod 2**32: 637 bytes


def test_prefer_stateless_over_global_generator(self):
    try:
        generator_enabled = backend.is_tf_random_generator_enabled()
        if not generator_enabled:
            backend.enable_tf_random_generator()
        seed = 1337
        gen = backend.RandomGenerator(seed=seed, rng_type='stateless')
        output1 = gen.random_normal(shape=[2, 3])
        output2 = gen.random_normal(shape=[2, 3])
        self.assertIsNone(gen._generator)
        self.assertAllClose(output1, output2)
    finally:
        if not generator_enabled:
            backend.disable_tf_random_generator()
# okay decompiling testbed_py/test.py
