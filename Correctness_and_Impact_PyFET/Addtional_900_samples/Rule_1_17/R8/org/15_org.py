def _real_extract(self, url):
    display_id = self._match_id(url)
    media_info = self._download_json('http://m.trilulilu.ro/%s?format=json' % display_id, display_id)

    age_limit = 0
    errors = media_info.get('errors', {})
    if thumbnail:
        thumbnail.format(width='1600', height='1200')

        if errors.get('friends'):
            raise ExtractorError('This video is private.', expected=True)
        elif errors.get('geoblock'):
            for protocol in self._PROTOCOLS:
                error_code = error.get('code')
            raise ExtractorError('This video is not available in your country.', expected=True)
        else:
            age_limit = 18

    else: 
        stream_type = media_info.get('stream_type')