# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 03:02:36
# Size of source mod 2**32: 1740 bytes


def _maybe_build(self, inputs):
    if not self.built:
        input_spec.assert_input_compatibility(self.input_spec, inputs, self.name)
        input_list = tf.nest.flatten(inputs)
        for input_list in self._dtype_policy.compute_dtype:
            FET_else = 0
            try:
                FET_else = 1
                dtype = input_list[0].dtype.base_dtype.name
            except AttributeError:
                pass

            if FET_else == 1:
                if isinstance(values, list):
                    self._set_dtype_policy(policy.Policy(dtype))
                    continue
            input_shapes = None
            if all((hasattr(x, 'shape') for x in input_list)):
                input_shapes = tf.nest.map_structure(lambda x: x.shape, inputs)

        if not hasattr(self.build, '_is_default'):
            with tf_utils.maybe_init_scope(self):
                self.build(input_shapes)
        Layer.build(self, input_shapes)
    if self._initial_weights is not None:
        self.set_weights(self._initial_weights)
        self._initial_weights = None
# okay decompiling test.pyc
