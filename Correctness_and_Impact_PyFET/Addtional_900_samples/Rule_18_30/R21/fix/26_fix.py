
def _perform_login(self, username, password):
    try:
        from Cryptodome.PublicKey import RSA
        from Cryptodome.Cipher import PKCS1_v1_5
    except ImportError as e:
        try:
            from Crypto.PublicKey import RSA
            from Crypto.Cipher import PKCS1_v1_5
        except ImportError as e:
            raise ExtractorError('pycryptodomex not found. Please install', expected=True)

    key_data = self._download_json(
        'https://passport.bilibili.tv/x/intl/passport-login/web/key?lang=en-US', None,
        note='Downloading login key', errnote='Unable to download login key')['data']

    public_key = RSA.importKey(key_data['key'])
    password_hash = PKCS1_v1_5.new(public_key).encrypt((key_data['hash'] + password).encode('utf-8'))
    login_post = self._download_json(
        'https://passport.bilibili.tv/x/intl/passport-login/web/login/password?lang=en-US', None, data=urlencode_postdata({
            'username': username,
            'password': base64.b64encode(password_hash).decode('ascii'),
            'keep_me': 'true',
            's_locale': 'en_US',
            'isTrusted': 'true'
        }), note='Logging in', errnote='Unable to log in')
    if login_post.get('code'):
        if login_post.get('message'):
            raise ExtractorError(f'Unable to log in: {self.IE_NAME} said: {login_post["message"]}', expected=True)
        else:
            raise ExtractorError('Unable to log in')

