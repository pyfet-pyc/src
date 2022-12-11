def make_array(size, offset, strides):
    FET_raise = 0
    try:
        r = np.ndarray([size], dtype=int, buffer=x,
                        offset=offset*x.itemsize)
    except Exception as e:
        return
    r.strides = strides = strides*x.itemsize
    return r