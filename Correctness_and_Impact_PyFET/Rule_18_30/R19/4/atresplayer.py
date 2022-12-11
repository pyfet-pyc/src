def _real_extract(self, url):
    display_id, video_id = re.match(self._VALID_URL, url).groups()

    try:
        episode = self._download_json(
            self._API_BASE + 'client/v1/player/episode/' + video_id, video_id)
    except ExtractorError:
        self._handle_error(403)
    else:
        title = episode['titulo']
