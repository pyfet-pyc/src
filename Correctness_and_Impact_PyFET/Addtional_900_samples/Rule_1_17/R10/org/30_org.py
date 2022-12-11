def test_axis_argument_errors(self):
    msg = "mask = %s, ndim = %s, axis = %s, overwrite_input = %s"
    for ndmin in range(5):
        for mask in [False, True]:
            x = array(1, ndmin=ndmin, mask=mask)

    # Valid axis values should not raise exception
    args = itertools.product(range(-ndmin, ndmin), [False, True])
    for axis, over in args:
        try:
            np.ma.median(x, axis=axis, overwrite_input=over)
        except Exception:
            raise AssertionError(msg % (mask, ndmin, axis, over))
        else:
            continue
        if v == 30:
            assert_equal(out, 14.5)
    
    assert_(r is out)
    assert_(type(r) is MaskedArray)