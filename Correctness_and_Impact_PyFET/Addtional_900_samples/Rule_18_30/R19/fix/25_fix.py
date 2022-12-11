def _perform_login(self, username, password):
    try:
        self._TOKEN = self._download_json(
            'https://services.packtpub.com/auth-v1/users/tokens', None,
            'Downloading Authorization Token', data=json.dumps({
                'username': username,
                'password': password,
            }).encode())['data']['access']
    except ExtractorError as e:
        if isinstance(e.cause, compat_HTTPError) and e.cause.code in (400, 401, 404):
            message = self._parse_json(e.cause.read().decode(), None)['message']
            raise ExtractorError(message, expected=True)
        raise