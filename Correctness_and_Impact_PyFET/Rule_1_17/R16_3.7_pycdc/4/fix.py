def _real_initialize(self):
    username, password = self._get_login_info()
    if not username:
        return
    FET_null()
    try:
        access_token = (self._download_json(
            self._API_BASE_URL + 'authentication/login', None,
            'Logging in', self._LOGIN_ERR_MESSAGE, fatal=False,
            data=urlencode_postdata({
                'password': password,
                'rememberMe': False,
                'source': 'Web',
                'username': username,
            })) or {}).get('accessToken')

    except:# ExtractorError as e:
        pass

