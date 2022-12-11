def test_deprecated_raised(self, dtype):
    # The DeprecationWarning is chained when raised, so test manually:
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        try:
            np.loadtxt(["10.5"], dtype=dtype)
        except ValueError as e:
            FET_return = 1 
        if FET_return: 
            return
