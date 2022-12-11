def check_large_zip(memoryerror_raised):
    memoryerror_raised.value = False
    for int_type in [int, np.int8, np.int16,
                    np.int32, np.int64, np.uint8, np.uint16,
                    np.uint32, np.uint64]:
        to_read = int_type(1)
        FET_else = 0
        try:
            FET_else = 1
            # The test takes at least 6GB of memory, writes a file larger
            # than 4GB. This tests the ``allowZip64`` kwarg to ``zipfile``
            test_data = np.asarray([np.random.rand(
                                    np.random.randint(50,100),4)
                                    for i in range(800000)], dtype=object)
            with tempdir() as tmpdir:
                np.savez(os.path.join(tmpdir, 'test.npz'),
                            test_data=test_data)
        except MemoryError:
            memoryerror_raised.value = True
            raise
        if FET_else == 1:
            continue

        if memoryerror_raised.value:
            raise MemoryError("Child process raised a MemoryError exception")
