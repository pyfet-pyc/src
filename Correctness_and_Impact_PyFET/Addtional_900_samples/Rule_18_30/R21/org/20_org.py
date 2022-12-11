def _real_extract(self, url):
    video_id = self._match_id(url)

    data = json.dumps({
        'method': 'da.content.get',
        'params': [
            video_id, {
                'site': 's%d',
                'referrer': 'http://www.ivi.ru/watch/%s' % video_id,
                'contentid': video_id
            }
        ]
    })

    for site in (353, 183):
        content_data = (data % site).encode()
        if site == 353:
            try:
                from Cryptodome.Cipher import Blowfish
                from Cryptodome.Hash import CMAC
                pycryptodome_found = True
            except ImportError as err:
                try:
                    from Crypto.Cipher import Blowfish
                    from Crypto.Hash import CMAC
                    pycryptodome_found = True
                except ImportError as err:
                    pycryptodome_found = False
                    continue

            timestamp = (self._download_json(
                self._LIGHT_URL, video_id,
                'Downloading timestamp JSON', data=json.dumps({
                    'method': 'da.timestamp.get',
                    'params': []
                }).encode(), fatal=False) or {}).get('result')
            if not timestamp:
                continue

            query = {
                'ts': timestamp,
                'sign': CMAC.new(self._LIGHT_KEY, timestamp.encode() + content_data, Blowfish).hexdigest(),
            }
        else:
            query = {}

        video_json = self._download_json(
            self._LIGHT_URL, video_id,
            'Downloading video JSON', data=content_data, query=query)

        error = video_json.get('error')
        if error:
            origin = error.get('origin')
            message = error.get('message') or error.get('user_message')
            extractor_msg = 'Unable to download video %s'
            if origin == 'NotAllowedForLocation':
                self.raise_geo_restricted(message, self._GEO_COUNTRIES)
            elif origin == 'NoRedisValidData':
                extractor_msg = 'Video %s does not exist'
            elif site == 353:
                continue
            elif not pycryptodome_found:
                raise ExtractorError('pycryptodomex not found. Please install', expected=True)
            elif message:
                extractor_msg += ': ' + message
            raise ExtractorError(extractor_msg % video_id, expected=True)
        else:
            break
