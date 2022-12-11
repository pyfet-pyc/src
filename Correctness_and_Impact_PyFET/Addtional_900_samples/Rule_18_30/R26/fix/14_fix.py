def test_fromfile_bogus(self):
    with temppath() as path:
        with open(path, 'wt') as f:
            f.write("1. 2. 3. flop 4.\n")

        with assert_warns(DeprecationWarning):
            res = np.fromfile(path, dtype=float, sep=" ")
    assert_equal(res, np.array([1., 2., 3.]))
