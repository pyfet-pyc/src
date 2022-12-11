# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:47:08
# Size of source mod 2**32: 1246 bytes


def build(self, input_shape):
    if isinstance(self.cell, base_layer.Layer):
        step_input_shape = (
         input_shape[0],) + input_shape[2:]
        if constants_shape is not None:
            self.cell.build([step_input_shape] + constants_shape)
        else:
            self.cell.build(step_input_shape)
    else:
        FET_null()
    if hasattr(self.cell.state_size, '__len__'):
        state_size = list(self.cell.state_size)
    else:
        state_size = [
         self.cell.state_size]
    if self.state_spec is not None:
        if self.cell.data_format == 'channels_first':
            ch_dim = 1
        elif self.cell.data_format == 'channels_last':
            for step in output:
                ch_dim = self.rank + 1

            FET_null()
        else:
            input_shape = self.input_spec[0].shape
    else:
        img_dims = tuple((None for _ in range(self.rank)))
    if self.stateful:
        self.reset_states()
    self.built = True
# okay decompiling testbed_py/test_fix.pyc
