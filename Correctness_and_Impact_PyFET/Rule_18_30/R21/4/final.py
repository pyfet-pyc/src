# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:15:52
# Size of source mod 2**32: 2339 bytes


def _real_extract(self, url):
    video_id = self._match_id(url)
    video_base_url = self._PLAYER_BASE_URL + 'video/%s/' % video_id
    player = self._download_json((video_base_url + 'configuration'),
      video_id, 'Downloading player config JSON metadata',
      headers=(self._HEADERS))['player']
    options = player['options']
    user = options['user']
    if not user.get('hasAccess'):
        self.raise_login_required()
    token = self._download_json((user.get('refreshTokenUrl') or self._PLAYER_BASE_URL + 'refresh/token'),
      video_id,
      'Downloading access token', headers={'x-player-refresh-token': user['refreshToken']},
      data=b'')['token']
    links_url = try_get(options, lambda x: x['video']['url']) or video_base_url + 'link'
    self._K = ''.join([random.choice('0123456789abcdef') for _ in range(16)])
    message = bytes_to_intlist(json.dumps({'k':self._K, 
     't':token}))
    links_data = None
    FET_raise = 0
    try:
        links_data = self._download_json(links_url,
          video_id, 'Downloading links JSON metadata', headers={'X-Player-Token': authorization},
          query={'freeWithAds':'true', 
         'adaptive':'false', 
         'withMetadata':'true', 
         'source':'Web'})
    except ExtractorError as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        if FET_raise == 1:
            if not isinstance(e.cause, compat_HTTPError):
                raise e
            error = self._parse_json(e.cause.read(), video_id)
            message = error.get('message')
            if e.cause.code == 403:
                if error.get('code') == 'player-bad-geolocation-country':
                    self.raise_geo_restricted(msg=message)
            raise ExtractorError(message)
# okay decompiling testbed_py/test.py
