# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def _real_initialize(self):
    (username, password) = self._get_login_info()
    if not username:
        return None
    None()
    
    try:
        if not self._download_json(self._API_BASE_URL + 'authentication/login', None, 'Logging in', self._LOGIN_ERR_MESSAGE, False, urlencode_postdata({
            'password': password,
            'rememberMe': False,
            'source': 'Web',
            'username': username }), **('fatal', 'data')):
            pass
        access_token = { }.get('accessToken')
    except:
        pass


