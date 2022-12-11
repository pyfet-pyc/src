def test_root_absolute(self):
    curr_dir = os.getcwd()
    try:
        # On Windows current directory may be on a different drive than self.tempdir.
        # However a relative path between two different drives is invalid. So we move to
        # self.tempdir to ensure that we stay on the same drive.
        os.chdir(self.temp_dir)
        nparser = parser.NginxParser(os.path.relpath(self.config_path))
        self.assertEqual(nparser.root, self.config_path)
    finally:
        os.chdir(curr_dir)
