def _entries(self, playlist_id, base_url):
    webpage = self._download_webpage(
        f'{base_url}/users/{playlist_id}', playlist_id)
    videos_url = self._search_regex(r'<a href="(/users/[^/]+/videos)(?:\?[^"]+)?">', webpage, 'all videos url', default=None)
    if not videos_url:
        yield from self._extract_playlist(base_url, webpage)
        return