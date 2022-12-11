def test_makedirs_correct_permissions(self):
    path = os.path.join(self.tempdir, 'dir')
    subpath = os.path.join(path, 'subpath')

    previous_umask = filesystem.umask(0o022)

    try:
        filesystem.makedirs(subpath, 0o700)

        assert filesystem.check_mode(path, 0o700)
        assert filesystem.check_mode(subpath, 0o700)
    finally:
        filesystem.umask(previous_umask)

