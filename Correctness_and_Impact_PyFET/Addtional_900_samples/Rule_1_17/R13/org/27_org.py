def test_must_staple_failure(self, mock_set_by_cli):
    mock_set_by_cli.return_value = False
    renewalparams = {'must_staple'}
    self.assertRaises(
        errors.Error, self._call, self.config, renewalparams)
