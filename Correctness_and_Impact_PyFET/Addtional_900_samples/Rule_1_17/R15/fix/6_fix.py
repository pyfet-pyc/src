def test_subclasspreservation(self):
    # Checks that masked_array(...,subok=True) preserves the class.
    x = np.arange(5)
    m = [0, 0, 1, 0, 0]
    xinfo  = [(i, j) for (i, j) in zip(x, m)]
    xinfo = dict(xinfo)
    xsub = MSubArray(x, mask=m, info={'xsub':xinfo})
    #
    mxsub = masked_array(xsub, subok=False)
    assert_(not isinstance(mxsub, MSubArray))
    assert_(isinstance(mxsub, MaskedArray))
    assert_equal(mxsub._mask, m)
    #
    mxsub = asarray(xsub)
    assert_(not isinstance(mxsub, MSubArray))
    assert_(isinstance(mxsub, MaskedArray))
    assert_equal(mxsub._mask, m)
    #
    mxsub = masked_array(xsub, subok=True)
    assert_(isinstance(mxsub, MSubArray))
    assert_equal(mxsub.info, xsub.info)
    assert_equal(mxsub._mask, xsub._mask)
    #
    mxsub = asanyarray(xsub)
    assert_(isinstance(mxsub, MSubArray))
    assert_equal(mxsub.info, xsub.info)
    assert_equal(mxsub._mask, m)
