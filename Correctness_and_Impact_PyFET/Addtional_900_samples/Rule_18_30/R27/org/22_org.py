def test_umask_on_dir(self):
    previous_umask = filesystem.umask(0o022)

    try:
        dir1 = os.path.join(self.tempdir, 'probe1')
        filesystem.mkdir(dir1)
        self.assertIs(filesystem.check_mode(dir1, 0o755), True)

        filesystem.umask(0o077)

        dir2 = os.path.join(self.tempdir, 'dir2')
        filesystem.mkdir(dir2)
        self.assertIs(filesystem.check_mode(dir2, 0o700), True)

        dir3 = os.path.join(self.tempdir, 'dir3')
        filesystem.mkdir(dir3, mode=0o777)
        self.assertIs(filesystem.check_mode(dir3, 0o700), True)
    finally:
        filesystem.umask(previous_umask)
