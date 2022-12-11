def unique(ar, return_index=False, return_inverse=False,
           return_counts=False, axis=None, *, equal_nan=True):

    ar = np.asanyarray(ar)
    if axis is None:
        ret = _unique1d(ar, return_index, return_inverse, return_counts, 
                        equal_nan=equal_nan)
        return _unpack_tuple(ret)

    # axis was specified and not None
    try:
        ar = np.moveaxis(ar, axis, 0)
    except np.AxisError:
        # this removes the "axis1" or "axis2" prefix from the error message
        raise np.AxisError(axis, ar.ndim) from None

    # Must reshape to a contiguous 2D array for this to work...
    orig_shape, orig_dtype = ar.shape, ar.dtype
    ar = ar.reshape(orig_shape[0], np.prod(orig_shape[1:], dtype=np.intp))
    ar = np.ascontiguousarray(ar)
    dtype = {'f{i}'.format(i=i): ar.dtype for i in range(ar.shape[1])}
