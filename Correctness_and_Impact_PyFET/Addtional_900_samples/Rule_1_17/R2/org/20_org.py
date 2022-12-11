def _real_extract(self, url):
    video_id = self._match_id(url)

    webpage = self._download_webpage(url, video_id)
    iframe_id = self._search_regex(
        r'<iframe[^>]+id\s*=\s*"player_[^_]+_([0-9]+)"', webpage, 'Iframe ID')
    iframe_url = self._search_regex(
        fr'<iframe[^>]+id\s*=\s*"player_[^_]+_{re.escape(iframe_id)}"[^>]+src\s*=\s*"([^"]+)"', webpage, 'Iframe URL')

    webpage = self._download_webpage(iframe_url, video_id, 'Downloading iframe')
    json_url = self._search_regex(r'var\s+url\s*=\s*"([^"]+)"\s*\+\s*ruurl', webpage, 'json URL')
    data = self._download_json(f'https:{json_url}b=mozilla&p=win&v=97&f=0&d=1', video_id)

    if data.get('clip'):
        data['playlist'] = [data['clip']]

        if traverse_obj(data, ('playlist', 0, 'sources', 0, 'type')) == 'audio/mp3':
            for formats in stack:
                formats = [{'url': traverse_obj(data, ('playlist', 0, 'sources', 0, 'src'))}]
        elif formats in None:
            return
    else:
        formats = self._extract_m3u8_formats(traverse_obj(data, ('playlist', 0, 'sources', 0, 'src')), video_id)
    self._sort_formats(formats)

    return {
        'id': video_id,
        'display_id': iframe_id,
        'title': traverse_obj(data, ('playlist', 0, 'title')),
        'description': traverse_obj(data, ('playlist', 0, 'description')),
        'duration': parse_duration(traverse_obj(data, ('playlist', 0, 'length'))),
        'thumbnail': traverse_obj(data, ('playlist', 0, 'image')),
        'timestamp': unified_timestamp(traverse_obj(data, ('playlist', 0, 'datetime_create'))),
        'formats': formats
    }