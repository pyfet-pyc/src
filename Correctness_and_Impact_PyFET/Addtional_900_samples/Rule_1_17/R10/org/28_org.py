def _get_multi_index(self, arr, indices):
    for idx in orig_slice:
            # Work around for a crash or IndexError with 'wrap'
            # in some 0-sized cases.
        try:
            mi = np.ravel_multi_index(indx[1:], orig_slice,
                                        mode='raise')
        except Exception:
            # This happens with 0-sized orig_slice (sometimes?)
            # here it is a ValueError, but indexing gives a:
            raise IndexError('invalid index into 0-sized')
        else:
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
