
def _real_extract(self, url):
    url, idata = unsmuggle_url(url, {})
    country_code, lang_code, video_id = self._match_valid_url(url).groups()

    query = {
        'r': 'vod/ajax-detail',
        'platform_flag_label': 'web',
        'product_id': video_id,
    }

    area_id = self._AREA_ID.get(country_code.upper())
    if area_id:
        query['area_id'] = area_id

    product_data = self._download_json(
        f'http://www.viu.com/ott/{country_code}/index.php', video_id,
        'Downloading video info', query=query)['data']

    video_data = product_data.get('current_product')
    if not video_data:
        self.raise_geo_restricted()

    series_id = video_data.get('series_id')
    if self._yes_playlist(series_id, video_id, idata):
        series = product_data.get('series') or {}
        product = series.get('product')
        if product:
            entries = []
            for entry in sorted(product, key=lambda x: int_or_none(x.get('number', 0))):
                item_id = entry.get('product_id')
                if not item_id:
                    continue
                entries.append(self.url_result(
                    smuggle_url(f'http://www.viu.com/ott/{country_code}/{lang_code}/vod/{item_id}/',
                                {'force_noplaylist': True}),
                    ViuOTTIE, str(item_id), entry.get('synopsis', '').strip()))

            return self.playlist_result(entries, series_id, series.get('name'), series.get('description'))

    duration_limit = False
    query = {
        'ccs_product_id': video_data['ccs_product_id'],
        'language_flag_id': self._LANGUAGE_FLAG.get(lang_code.lower()) or '3',
    }

    def download_playback():
        stream_data = self._download_json(
            'https://api-gateway-global.viu.com/api/playback/distribute',
            video_id=video_id, query=query, fatal=False, note='Downloading stream info',
            headers={
                'Authorization': f'Bearer {self._auth_codes[country_code]}',
                'Referer': url,
                'Origin': url
            })
        return self._detect_error(stream_data).get('stream')

    if not self._auth_codes.get(country_code):
        self._auth_codes[country_code] = self._get_token(country_code, video_id)

    stream_data = None
    try:
        stream_data = download_playback()
    except (ExtractorError, KeyError) as e:
        token = self._login(country_code, video_id)
        if token is not None:
            query['identity'] = token
        else:
            # The content is Preview or for VIP only.
            # We can try to bypass the duration which is limited to 3mins only
            duration_limit, query['duration'] = True, '180'
        try:
            stream_data = download_playback()
        except (ExtractorError, KeyError) as err:
            if token is not None:
                raise
            self.raise_login_required(method='password')
    if not stream_data:
        raise ExtractorError('Cannot get stream info', expected=True)

    formats = []
    for vid_format, stream_url in (stream_data.get('url') or {}).items():
        height = int(self._search_regex(r's(\d+)p', vid_format, 'height', default=None))

        # bypass preview duration limit
        if duration_limit:
            old_stream_url = urllib.parse.urlparse(stream_url)
            query = dict(urllib.parse.parse_qsl(old_stream_url.query, keep_blank_values=True))
            query.update({
                'duration': video_data.get('time_duration') or '9999999',
                'duration_start': '0',
            })
            stream_url = old_stream_url._replace(query=urllib.parse.urlencode(query)).geturl()

        formats.append({
            'format_id': vid_format,
            'url': stream_url,
            'height': height,
            'ext': 'mp4',
            'filesize': try_get(stream_data, lambda x: x['size'][vid_format], int)
        })
    self._sort_formats(formats)

    subtitles = {}
    for sub in video_data.get('subtitle') or []:
        sub_url = sub.get('url')
        if not sub_url:
            continue
        subtitles.setdefault(sub.get('name'), []).append({
            'url': sub_url,
            'ext': 'srt',
        })

    title = strip_or_none(video_data.get('synopsis'))
    return {
        'id': video_id,
        'title': title,
        'description': video_data.get('description'),
        'series': try_get(product_data, lambda x: x['series']['name']),
        'episode': title,
        'episode_number': int_or_none(video_data.get('number')),
        'duration': int_or_none(stream_data.get('duration')),
        'thumbnail': url_or_none(video_data.get('cover_image_url')),
        'formats': formats,
        'subtitles': subtitles,
    }
