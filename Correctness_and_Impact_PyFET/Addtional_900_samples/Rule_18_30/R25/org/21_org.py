def compare_model(model1_func, model2_func, test_image, check_blobs):
    ''' model_func(test_image, check_blobs)
    '''
    cb1, cb2 = check_blobs, check_blobs
    if isinstance(check_blobs, dict):
        cb1 = check_blobs.keys()
        cb2 = check_blobs.values()
    print('Running the first model...')
    res1 = model1_func(test_image, check_blobs)
    print('Running the second model...')
    res2 = model2_func(test_image, check_blobs)
    for idx in range(len(cb1)):
        print('Checking {} -> {}...'.format(cb1[idx], cb2[idx]))
        n1, n2 = cb1[idx], cb2[idx]
        r1 = res1[n1] if n1 in res1 else None
        r2 = res2[n2] if n2 in res2 else None
        assert r1 is not None or r2 is None, \
            "Blob {} in model1 is None".format(n1)
        assert r2 is not None or r1 is None, \
            "Blob {} in model2 is None".format(n2)
        assert r1.shape == r2.shape, \
            "Blob {} and {} shape mismatched: {} vs {}".format(
                n1, n2, r1.shape, r2.shape)

        np.testing.assert_array_almost_equal(
            r1, r2, decimal=3,
            err_msg='{} and {} not matched. Max diff: {}'.format(
                n1, n2, np.amax(np.absolute(r1 - r2))))

    return True