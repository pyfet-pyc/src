def test_umask_on_file(self):
    previous_umask = filesystem.umask(0o022)

    try:
        file1 = os.path.join(self.tempdir, 'probe1')
        UmaskTest._create_file(file1)
        self.assertIs(filesystem.check_mode(file1, 0o755), True)

        filesystem.umask(0o077)

        file2 = os.path.join(self.tempdir, 'probe2')
        UmaskTest._create_file(file2)
        self.assertIs(filesystem.check_mode(file2, 0o700), True)

        file3 = os.path.join(self.tempdir, 'probe3')
        UmaskTest._create_file(file3)
        self.assertIs(filesystem.check_mode(file3, 0o700), True)
    finally:
        filesystem.umask(previous_umask)
