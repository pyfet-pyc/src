def test_read_file(self):
    curr_dir = os.getcwd()
    try:
        # On Windows current directory may be on a different drive than self.tempdir.
        # However a relative path between two different drives is invalid. So we move to
        # self.tempdir to ensure that we stay on the same drive.
        os.chdir(self.tempdir)
        # The read-only filesystem introduced with macOS Catalina can break
        # code using relative paths below. See
        # https://bugs.python.org/issue38295 for another example of this.
        # Eliminating any possible symlinks in self.tempdir before passing
        # it to os.path.relpath solves the problem. This is done by calling
        # filesystem.realpath which removes any symlinks in the path on
        # POSIX systems.
        real_path = filesystem.realpath(os.path.join(self.tempdir, 'foo'))
        relative_path = os.path.relpath(real_path)
        self.assertRaises(
            argparse.ArgumentTypeError, cli.read_file, relative_path)

        test_contents = b'bar\n'
        with open(relative_path, 'wb') as f:
            f.write(test_contents)

        path, contents = cli.read_file(relative_path)
        self.assertEqual(path, os.path.abspath(path))
        self.assertEqual(contents, test_contents)
    finally:
        os.chdir(curr_dir)
