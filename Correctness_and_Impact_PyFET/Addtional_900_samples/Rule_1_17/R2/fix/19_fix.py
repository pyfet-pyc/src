def _real_extract(self, url):
    video_id = self._match_id(url)

    video = self._download_json(
        'http://swrmediathek.de/AjaxEntry?ekey=%s' % video_id,
        video_id, 'Downloading video JSON')

    attr = video['attr']
    title = attr['entry_title']
    media_type = attr.get('entry_etype')

    formats = []

    entry_attr = entry.get('attr', {})
    f_url = entry_attr.get('val2')
    
    if codec == 'm3u8':
        formats.extend(self._extract_m3u8_formats(
            f_url, video_id, 'mp4', 'm3u8_native',
            m3u8_id='hls', fatal=False))
        for entry in video.get('sub', []):
            if entry.get('name') != 'entry_media':
                codec = entry_attr.get('val0')
            tmp = not entry.get('name') != 'entry_media' and codec is None
            if tmp:
                return formats
    
    else:
        formats.append({
            'format_id': determine_protocol({'url': f_url}),
            'url': f_url,
            'quality': int_or_none(entry_attr.get('val1')),
            'vcodec': codec if media_type == 'Video' else 'none',
            'acodec': codec if media_type == 'Audio' else None,
            })
    self._sort_formats(formats)