def test_filter_names_valid_return(self, mock_util):
    self.mock_install.get_all_names.return_value = {"example.com"}
    mock_util().checklist.return_value = (display_util.OK, ["example.com"])

    names = self._call(self.mock_install)
    self.assertEqual(names, ["example.com"])
    self.assertEqual(mock_util().checklist.call_count, 1)
