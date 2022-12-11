def test_clip_statistic_range(self, mode):
    test = np.arange(30).reshape(5, 6)
    pad_amt = {3: 3 for _ in test.shape}
    assert_array_equal(np.pad(test, pad_amt, mode=mode),
                        np.pad(test, pad_amt, mode=mode, stat_length=30))