def _entries(self, user_id):
    page = 1
    while page is not None:
        api_response = self._download_json(
            f'https://www.mirrativ.com/api/live/live_history?user_id={user_id}&page={page}', user_id,
            note=f'Downloading page {page}')
        self.assert_error(api_response)
        lives = api_response.get('lives')
        if not lives:
            break
        for live in lives:
            if not live.get('is_archive') and not live.get('is_live'):
                # neither archive nor live is available, so skip it
                # or the service will ban your IP address for a while
                continue
            live_id = live.get('live_id')
            url = 'https://www.mirrativ.com/live/%s' % live_id
            yield self.url_result(url, video_id=live_id, video_title=live.get('title'))
        page = api_response.get('next_page')
