def test_freshen_update(self, _):
    hosts_file = os.path.join(self.test_dir, "hosts")
    hosts_data = "This data should not be overwritten"

    with self.mock_property("updateHostsFile.BASEDIR_PATH"):
        updateHostsFile.BASEDIR_PATH = self.test_dir

        with open(hosts_file, "w") as f:
            f.write(hosts_data)

        dir_count = self.dir_count

        for update_auto in (False, True):
            update_sources = prompt_for_update(
                freshen=True, update_auto=update_auto
            )
            self.assertTrue(update_sources)

            output = sys.stdout.getvalue()
            self.assertEqual(output, "")

            sys.stdout = StringIO()

            self.assertEqual(self.dir_count, dir_count)

            with open(hosts_file, "r") as f:
                contents = f.read()
                self.assertEqual(contents, hosts_data)
