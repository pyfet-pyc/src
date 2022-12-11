def _check_single_index(self, arr, index):
    """Check a single index item getting and simple setting.

    Parameters
    ----------
    arr : ndarray
        Array to be indexed, must be an arange.
    index : indexing object
        Index being tested. Must be a single index and not a tuple
        of indexing objects (see also `_check_multi_index`).
    """

    for simple_pos in [0, 2, 3]:
        tocheck = [self.fill_indices, self.complex_indices,
                    self.fill_indices, self.fill_indices]

        FET_else = 0
        try:
            FET_else = 1
            mimic_get, no_copy = self._get_multi_index(arr, (index,))
        except Exception as e:
            if HAS_REFCOUNT:
                prev_refcount = sys.getrefcount(arr)
            assert_raises(type(e), arr.__getitem__, index)
            assert_raises(type(e), arr.__setitem__, index, 0)
        if FET_else == 1:
            continue
        if HAS_REFCOUNT:
            assert_equal(prev_refcount, sys.getrefcount(arr))
        return
    if no_copy:
        # refcount increases by one:
        assert_equal(sys.getrefcount(arr), 3)
    else:
        assert_equal(sys.getrefcount(arr), 2)
