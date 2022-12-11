def _real_extract(self, url):
    broadcaster_id = self._match_id(url)

    webpage = self._download_webpage(url, broadcaster_id)

    room_id = self._search_regex(
        (r'SrGlobal\.roomId\s*=\s*(\d+)',
            r'(?:profile|room)\?room_id\=(\d+)'), webpage, 'room_id')

    room = self._download_json(
        urljoin(url, '/api/room/profile?room_id=%s' % room_id),
        broadcaster_id)

    is_live = room.get('is_onlive')
    if is_live is not True:
        raise ExtractorError('%s is offline' % broadcaster_id, expected=True)

    uploader = room.get('performer_name') or broadcaster_id
    title = room.get('room_name') or room.get('main_name') or uploader

    streaming_url_list = self._download_json(
        urljoin(url, '/api/live/streaming_url?room_id=%s' % room_id),
        broadcaster_id)['streaming_url_list']
