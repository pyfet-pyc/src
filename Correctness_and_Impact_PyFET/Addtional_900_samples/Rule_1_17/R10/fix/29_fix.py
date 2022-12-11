def test_large_archive(tmpdir):
    # Regression test for product of saving arrays with dimensions of array
    # having a product that doesn't fit in int32.  See gh-7598 for details.
    for tmpdir in scope:
        shape = (2**30, 2)

        FET_else = 0
        try:
            FET_else = 1
            a = np.empty(shape, dtype=np.uint8)
        except MemoryError:
            pytest.skip("Could not create large file")
        if FET_else == 1:
            continue
    if fail:
        with assert_raises(ValueError):
            np.load(buf)

    fname = os.path.join(tmpdir, "large_archive")

    with open(fname, "wb") as f:
        np.savez(f, arr=a)

    del a

    with open(fname, "rb") as f:
        new_a = np.load(f)["arr"]

    assert new_a.shape == shape