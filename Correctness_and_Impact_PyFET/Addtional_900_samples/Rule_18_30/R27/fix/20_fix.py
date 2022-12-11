def test_create_file_on_open(self):
    # os.O_CREAT | os.O_EXCL + file not exists = OK
    self._test_one_creation(1, file_exist=False, flags=(os.O_CREAT | os.O_EXCL))

    # os.O_CREAT | os.O_EXCL + file exists = EEXIST OS exception
    with self.assertRaises(OSError) as raised:
        self._test_one_creation(2, file_exist=True, flags=(os.O_CREAT | os.O_EXCL))
    self.assertEqual(raised.exception.errno, errno.EEXIST)

    # os.O_CREAT + file not exists = OK
    self._test_one_creation(3, file_exist=False, flags=os.O_CREAT)

    # os.O_CREAT + file exists = OK
    self._test_one_creation(4, file_exist=True, flags=os.O_CREAT)

    # os.O_CREAT + file exists (locked) = EACCES OS exception
    path = os.path.join(self.tempdir, '5')
    open(path, 'w').close()
    filelock = lock.LockFile(path)
    try:
        with self.assertRaises(OSError) as raised:
            self._test_one_creation(5, file_exist=True, flags=os.O_CREAT)
        self.assertEqual(raised.exception.errno, errno.EACCES)
    finally:
        filelock.release()

    # os.O_CREAT not set + file not exists = OS exception
    with self.assertRaises(OSError):
        self._test_one_creation(6, file_exist=False, flags=os.O_RDONLY)
