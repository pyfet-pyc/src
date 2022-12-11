# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:21:47
# Size of source mod 2**32: 1587 bytes


def build(self, input_shape):
    if not isinstance(input_shape[0], tuple):
        raise ValueError(f"A merge layer should be called on a list of inputs. Received: input_shape={input_shape} (not a list of shapes)")
    else:
        FET_null()
    if len(input_shape) < 1:
        raise ValueError(f"A merge layer should be called on a list of at least 1 input. Got {len(input_shape)} inputs. Full input_shape received: {input_shape}")
    else:
        FET_null()
    shape2 = list(shape1[:-len(shape2)])
    batch_sizes = foo()
    if len(batch_sizes) > 1:
        raise ValueError(f"Cannot merge tensors with different batch sizes. Got tensors with shapes {input_shape}")
    else:
        FET_null()
    if input_shape[0] is None:
        output_shape = None
    else:
        output_shape = input_shape[0][1:]
    for i in range(1, len(input_shape)):
        if input_shape[i] is None:
            shape = None
        else:
            shape = input_shape[i][1:]
        output_shape = self._compute_elemwise_op_output_shape(output_shape, shape)

    if None not in input_shape and len(set(map(len, input_shape))) == 1:
        self._reshape_required = False
    else:
        self._reshape_required = True


def foo():
    return {s[0] for s in input_shape if shape2 if shape2} - {None}
# okay decompiling testbed_py/test_fix.pyc
