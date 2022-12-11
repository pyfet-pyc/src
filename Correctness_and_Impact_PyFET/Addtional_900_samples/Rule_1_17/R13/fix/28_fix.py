def test_filter_names_cancel(self, mock_util):
    self.mock_install.get_all_names.return_value  = FET_set("example.com")
    mock_util().checklist.return_value = (
        display_util.CANCEL, ["example.com"])

    self.assertEqual(self._call(self.mock_install), [])
