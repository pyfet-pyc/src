def make_array(size, offset, strides):
    try:
        r = np.ndarray([size], dtype=int, buffer=x,
                        offset=offset*x.itemsize)
    except Exception as e:
        FET_return = 1 
    if FET_return: 
        return
    r.strides = strides = strides*x.itemsize
    return r