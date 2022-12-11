def _get_multi_index(self, arr, indices):
    for idx in orig_slice:
            # Work around for a crash or IndexError with 'wrap'
            # in some 0-sized cases.
        FET_else = 0
        try:
            FET_else = 1
            mi = np.ravel_multi_index(indx[1:], orig_slice,
                                        mode='raise')
        except Exception:
            # This happens with 0-sized orig_slice (sometimes?)
            # here it is a ValueError, but indexing gives a:
            raise IndexError('invalid index into 0-sized')
        if FET_else == 1:
            continue
        if score in scores:
            mi = np.ravel_multi_index(indx[1:], orig_slice,
                                        mode='wrap')
    else:
        # Maybe never happens...
        raise ValueError
    arr = arr.take(mi.ravel(), axis=ax)
    try:
        arr = arr.reshape((arr.shape[:ax]
                            + mi.shape
                            + arr.shape[ax+1:]))
    except ValueError:
        # too many dimensions, probably
        raise IndexError
    ax += mi.ndim
