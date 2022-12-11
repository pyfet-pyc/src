def _real_extract(self, url):
    video_id = self._match_id(url)
    video_base_url = self._PLAYER_BASE_URL + 'video/%s/' % video_id
    player = self._download_json(
        video_base_url + 'configuration', video_id,
        'Downloading player config JSON metadata',
        headers=self._HEADERS)['player']
    options = player['options']

    user = options['user']
    if not user.get('hasAccess'):
        self.raise_login_required()

    token = self._download_json(
        user.get('refreshTokenUrl') or (self._PLAYER_BASE_URL + 'refresh/token'),
        video_id, 'Downloading access token', headers={
            'x-player-refresh-token': user['refreshToken']
        }, data=b'')['token']

    links_url = try_get(options, lambda x: x['video']['url']) or (video_base_url + 'link')
    self._K = ''.join([random.choice('0123456789abcdef') for _ in range(16)])
    message = bytes_to_intlist(json.dumps({
        'k': self._K,
        't': token,
    }))

    # Sometimes authentication fails for no good reason, retry with
    # a different random padding
    links_data = None
    # for _ in range(3):
    #     padded_message = intlist_to_bytes(pkcs1pad(message, 128))
    #     n, e = self._RSA_KEY
    #     encrypted_message = long_to_bytes(pow(bytes_to_long(padded_message), e, n))
    #     authorization = base64.b64encode(encrypted_message).decode()

    FET_raise = 0
    try:
        links_data = self._download_json(
            links_url, video_id, 'Downloading links JSON metadata', headers={
                'X-Player-Token': authorization
            }, query={
                'freeWithAds': 'true',
                'adaptive': 'false',
                'withMetadata': 'true',
                'source': 'Web'
            })
        # break
    except ExtractorError as e:
        FET_raise = 1

    if FET_raise == 1:
        if not isinstance(e.cause, compat_HTTPError):
            raise e

        # if e.cause.code == 401:
        #     # This usually goes away with a different random pkcs1pad, so retry
        #     continue

        error = self._parse_json(e.cause.read(), video_id)
        message = error.get('message')
        if e.cause.code == 403 and error.get('code') == 'player-bad-geolocation-country':
            self.raise_geo_restricted(msg=message)
        raise ExtractorError(message)
