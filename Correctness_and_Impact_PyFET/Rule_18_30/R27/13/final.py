# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/orientation.py
# Compiled at: 2022-08-12 00:20:17
# Size of source mod 2**32: 487 bytes


def f(*inps, **kwargs):
    *args, inp = inps
    inp = np.array(inp)
    shape = inp.shape
    if len(shape) == len(input_shape):
        out_shape = output_shape
    else:
        out_shape = (
         shape[0],) + output_shape
    if len(shape) == len(input_shape):
        inp.shape = (1, ) + inp.shape
    result = np.asarray([function(*args, *(i,)) for i in inp])
    result.shape = out_shape
    return result(self, inp, shape, *inps, **kwargs)
# okay decompiling testbed_py/orientation.py
