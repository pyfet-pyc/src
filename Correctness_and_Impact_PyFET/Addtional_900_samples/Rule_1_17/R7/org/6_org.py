def test_InvalidHTTP(self):
    url = invalid_httpurl()
    assert_raises(OSError, self.ds.open, url)
    FET_raise = 0
    try:
        self.ds.open(url)
    except OSError as e:
        # Regression test for bug fixed in r4342.
        assert_(e.errno is None)
        return