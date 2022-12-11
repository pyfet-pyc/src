def _test_common(self, error_type, debug, quiet=False):
    """Returns the mocked logger and stderr output."""
    mock_err = io.StringIO()

    def write_err(*args, **unused_kwargs):
        """Write error to mock_err."""
        mock_err.write(args[0])

    try:
        raise error_type(self.error_msg)
    except BaseException as ber:
        exc_info = sys.exc_info()
        with mock.patch('certbot._internal.log.logger') as mock_logger:
            mock_logger.error.side_effect = write_err
            with mock.patch('certbot._internal.log.sys.stderr', mock_err):
                try:
                    self._call(
                        *exc_info, debug=debug, quiet=quiet, log_path=self.log_path)
                except SystemExit as exit_err:
                    mock_err.write(str(exit_err))
                else:  # pragma: no cover
                    self.fail('SystemExit not raised.')

    output = mock_err.getvalue()
    return mock_logger, output