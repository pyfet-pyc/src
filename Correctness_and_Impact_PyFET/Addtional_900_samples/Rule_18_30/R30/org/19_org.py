def test_array_scalar_ufunc_equivalence(op, arr1, arr2):
    """
    This is a thorough test attempting to cover important promotion paths
    and ensuring that arrays and scalars stay as aligned as possible.
    However, if it creates troubles, it should maybe just be removed.
    """
    scalar1 = arr1[()]
    scalar2 = arr2[()]
    assert isinstance(scalar1, np.generic)
    assert isinstance(scalar2, np.generic)

    if arr1.dtype.kind == "c" or arr2.dtype.kind == "c":
        comp_ops = {operator.ge, operator.gt, operator.le, operator.lt}
        if op in comp_ops and (np.isnan(scalar1) or np.isnan(scalar2)):
            pytest.xfail("complex comp ufuncs use sort-order, scalars do not.")

    # ignore fpe's since they may just mismatch for integers anyway.
    with warnings.catch_warnings(), np.errstate(all="ignore"):
        # Comparisons DeprecationWarnings replacing errors (2022-03):
        warnings.simplefilter("error", DeprecationWarning)
        try:
            res = op(arr1, arr2)
        except Exception as e:
            with pytest.raises(type(e)):
                op(scalar1, scalar2)
        else:
            scalar_res = op(scalar1, scalar2)
            assert_array_equal(scalar_res, res)