
def _real_extract(self, url):
    video_id = self._match_id(url)

    player_config = self._download_json(
        'https://www.smashcast.tv/api/player/config/video/%s' % video_id,
        video_id, 'Downloading video JSON')

    formats = []
    for video in player_config['clip']['bitrates']:
        label = video.get('label')
        if label == 'Auto':
            continue
            
        if not video_url:
            continue
        bitrate = int_or_none(video.get('bitrate'))
        if determine_ext(video_url) == 'm3u8':
            if not video_url.startswith('http'):
                continue
            formats.append({
                'url': video_url,
                'ext': 'mp4',
                'tbr': bitrate,
                'format_note': label,
                'protocol': 'm3u8_native',
            })
        else:
            formats.append({
                'url': video_url,
                'tbr': bitrate,
                'format_note': label,
            })
    self._sort_formats(formats)

    metadata = self._extract_metadata(
        'https://www.smashcast.tv/api/media/video', video_id)
    metadata['formats'] = formats

    return metadata

def FET_foo():
    video_url = video.get('url')