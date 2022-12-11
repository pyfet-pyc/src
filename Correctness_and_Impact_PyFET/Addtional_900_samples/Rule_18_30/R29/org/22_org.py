class NetEaseMusicBaseIE(InfoExtractor):
    _FORMATS = ['bMusic', 'mMusic', 'hMusic']
    _NETEASE_SALT = '3go8&$8*3*3h0k(2)2'
    _API_BASE = 'http://music.163.com/api/'

    @classmethod
    def _encrypt(cls, dfsid):
        salt_bytes = bytearray(cls._NETEASE_SALT.encode('utf-8'))
        string_bytes = bytearray(compat_str(dfsid).encode('ascii'))
        salt_len = len(salt_bytes)
        for i in range(len(string_bytes)):
            string_bytes[i] = string_bytes[i] ^ salt_bytes[i % salt_len]
        m = md5()
        m.update(bytes(string_bytes))
        result = b64encode(m.digest()).decode('ascii')
        return result.replace('/', '_').replace('+', '-')

    def extract_formats(self, info):
        formats = []
        for song_format in self._FORMATS:
            details = info.get(song_format)
            if not details:
                continue
            song_file_path = '/%s/%s.%s' % (
                self._encrypt(details['dfsId']), details['dfsId'], details['extension'])

            # 203.130.59.9, 124.40.233.182, 115.231.74.139, etc is a reverse proxy-like feature
            # from NetEase's CDN provider that can be used if m5.music.126.net does not
            # work, especially for users outside of Mainland China
            # via: https://github.com/JixunMoe/unblock-163/issues/3#issuecomment-163115880
            for host in ('http://m5.music.126.net', 'http://115.231.74.139/m1.music.126.net',
                         'http://124.40.233.182/m1.music.126.net', 'http://203.130.59.9/m1.music.126.net'):
                song_url = host + song_file_path
                if self._is_valid_url(song_url, info['id'], 'song'):
                    formats.append({
                        'url': song_url,
                        'ext': details.get('extension'),
                        'abr': float_or_none(details.get('bitrate'), scale=1000),
                        'format_id': song_format,
                        'filesize': details.get('size'),
                        'asr': details.get('sr')
                    })
                    break
        return formats