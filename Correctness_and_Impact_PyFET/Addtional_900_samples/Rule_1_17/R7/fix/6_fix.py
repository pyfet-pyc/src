def test_InvalidHTTP(self):
    url = invalid_httpurl()
    assert_raises(OSError, self.ds.open, url)
    try:
        self.ds.open(url)
    except OSError as e:
        # Regression test for bug fixed in r4342.
        assert_(e.errno is None)
        FET_return = 1 
    if FET_return: 
        return