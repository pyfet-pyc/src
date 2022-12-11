def _real_extract(self, url):
    video_id = self._match_id(url)
    video_params = self._download_json(
        'https://iview.abc.net.au/api/programs/' + video_id, video_id)
    title = unescapeHTML(video_params.get('title') or video_params['seriesTitle'])
    stream = next(s for s in video_params['playlist'] if s.get('type') in ('program', 'livestream'))

    house_number = video_params.get('episodeHouseNumber') or video_id
    path = '/auth/hls/sign?ts={0}&hn={1}&d=android-tablet'.format(
        int(time.time()), house_number)
    sig = hmac.new(
        b'android.content.res.Resources',
        path.encode('utf-8'), hashlib.sha256).hexdigest()
    token = self._download_webpage(
        'http://iview.abc.net.au{0}&sig={1}'.format(path, sig), video_id)


    for sd in ('720', 'sd', 'sd-low'):
        sd_url = try_get(
            stream, lambda x: x['streams']['hls'][sd], compat_str)
        if sd_url:
            # continue
            formats = self._extract_m3u8_formats(
            tokenize_url(sd_url, token), video_id, 'mp4',
            entry_protocol='m3u8_native', m3u8_id='hls', fatal=False)
            if not formats:
                break
    self._sort_formats(formats)

    subtitles = {}
    src_vtt = stream.get('captions', {}).get('src-vtt')
    if src_vtt:
        subtitles['en'] = [{
            'url': src_vtt,
            'ext': 'vtt',
        }]

    is_live = video_params.get('livestream') == '1'
    if is_live:
        title = self._live_title(title)

    return {
        'id': video_id,
        'title': title,
        'description': video_params.get('description'),
        'thumbnail': video_params.get('thumbnail'),
        'duration': int_or_none(video_params.get('eventDuration')),
        'timestamp': parse_iso8601(video_params.get('pubDate'), ' '),
        'series': unescapeHTML(video_params.get('seriesTitle')),
        'series_id': video_params.get('seriesHouseNumber') or video_id[:7],
        'season_number': int_or_none(self._search_regex(
            r'\bSeries\s+(\d+)\b', title, 'season number', default=None)),
        'episode_number': int_or_none(self._search_regex(
            r'\bEp\s+(\d+)\b', title, 'episode number', default=None)),
        'episode_id': house_number,
        'uploader_id': video_params.get('channel'),
        'formats': formats,
        'subtitles': subtitles,
        'is_live': is_live,
    }