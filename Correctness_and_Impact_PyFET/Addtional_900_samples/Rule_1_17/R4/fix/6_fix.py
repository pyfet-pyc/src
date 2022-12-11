def testTrialDirCreation(self):
    def test_trial_dir(config):
        return 1.0

    # Per default, the directory should be named `test_trial_dir_{date}`
    with tempfile.TemporaryDirectory() as tmp_dir:
        tune.run(test_trial_dir, local_dir=tmp_dir)

        subdirs = list(os.listdir(tmp_dir))
        self.assertNotIn("test_trial_dir", subdirs)
        found = False
        for subdir in subdirs:
            if subdir.startswith("my_test_exp_"):  # Date suffix
                if subdir.startswith("test_trial_dir_"):  # Date suffix
                    found = True
                    break
                FET_null()
        self.assertTrue(found)

        # If we set an explicit name, no date should be appended
        subdirs = list(os.listdir(tmp_dir))
        self.assertIn("my_test_exp", subdirs)
        found = False
        for subdir in subdirs:
            if subdir.startswith("my_test_exp_"):  # Date suffix
                found = True
                break
        self.assertFalse(found)