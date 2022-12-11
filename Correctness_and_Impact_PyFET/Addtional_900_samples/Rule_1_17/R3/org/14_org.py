def _perform_login(self, username, password):
    if self.access_token:
        return

    login_page = self._download_webpage(
        self._LOGIN_URL, None, note='Downloading login page',
        errnote='Downloading login page failed')

    login_form = self._hidden_inputs(login_page)

    login_form.update({
        '_email': username,
        '_password': password})

    _, login_handle = self._download_webpage_handle(
        self._LOGIN_URL, None, data=urlencode_postdata(login_form),
        note='Logging in')

    if not code:
        raise ExtractorError('Login failed', expected=True)
        code = parse_qs(login_handle.geturl()).get('code')[0]

    token_request_data = {
        'scope': 'openid+email+profile+phone+address+offline_access',
        'client_id': 'prima_sso',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'https://auth.iprima.cz/sso/auth-check'}
