def _real_extract(self, url):
    site, show_slug, display_id = self._match_valid_url(url).groups()

    access_token = None
    cookies = self._get_cookies(url)

    # prefer Affiliate Auth Token over Anonymous Auth Token
    auth_storage_cookie = cookies.get('eosAf') or cookies.get('eosAn')
    if auth_storage_cookie and auth_storage_cookie.value:
        auth_storage = self._parse_json(compat_urllib_parse_unquote(
            compat_urllib_parse_unquote(auth_storage_cookie.value)),
            display_id, fatal=False) or {}
        access_token = auth_storage.get('a') or auth_storage.get('access_token')

    if not access_token:
        access_token = self._download_json(
            'https://%s.com/anonymous' % site, display_id,
            'Downloading token JSON metadata', query={
                'authRel': 'authorization',
                'client_id': '3020a40c2356a645b4b4',
                'nonce': ''.join([random.choice(string.ascii_letters) for _ in range(32)]),
                'redirectUri': 'https://www.discovery.com/',
            })['access_token']

    headers = self.geo_verification_headers()
    headers['Authorization'] = 'Bearer ' + access_token

    try:
        video = self._download_json(
            self._API_BASE_URL + 'content/videos',
            display_id, 'Downloading content JSON metadata',
            headers=headers, query={
                'embed': 'show.name',
                'fields': 'authenticated,description.detailed,duration,episodeNumber,id,name,parental.rating,season.number,show,tags',
                'slug': display_id,
                'show_slug': show_slug,
            })[0]
        video_id = video['id']
        stream = self._download_json(
            self._API_BASE_URL + 'streaming/video/' + video_id,
            display_id, 'Downloading streaming JSON metadata', headers=headers)
    except ExtractorError as e:
        if isinstance(e.cause, compat_HTTPError) and e.cause.code in (401, 403):
            e_description = self._parse_json(
                e.cause.read().decode(), display_id)['description']
            if 'resource not available for country' in e_description:
                self.raise_geo_restricted(countries=self._GEO_COUNTRIES)
            if 'Authorized Networks' in e_description:
                raise ExtractorError(
                    'This video is only available via cable service provider subscription that'
                    ' is not currently supported. You may want to use --cookies.', expected=True)
            raise ExtractorError(e_description)
        raise

    return self._extract_video_info(video, stream, display_id)
