# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:39:27
# Size of source mod 2**32: 1385 bytes


def na_logical_op(x: np.ndarray, y, op):
    try:
        result = op(x, y)
    except TypeError:
        x = ensure_object(x)
        y = ensure_object(y)
        result = libops.vec_binop(x.ravel(), y.ravel(), op)
        if not isna(y):
            y = bool(y)
        FET_raise = 0
        try:
            result = libops.scalar_binop(x, y, op)
        except (TypeError,
         ValueError,
         AttributeError,
         OverflowError,
         NotImplementedError) as err:
            try:
                FET_raise = 1
            finally:
                err = None
                del err

        else:
            FET_null()
        if FET_raise == 1:
            typ = type(y).__name__
            raise TypeError(f"Cannot perform '{op.__name__}' with a dtyped [{x.dtype}] array and scalar of type [{typ}]")
    else:
        FET_null()
    return result.reshape(x.shape)
# okay decompiling testbed_py/test.py
