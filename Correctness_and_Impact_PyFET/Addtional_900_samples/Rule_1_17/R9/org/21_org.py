
def _entries(self, id):
    last = None

    while itertools.count():
        channel_json = self._download_json(
            f'https://api.divulg.org/organization/{id}/posts', id, headers={'accept': 'application/json, text/plain, */*'},
            query={'after': last} if last else {}, note=f'Downloading Page {page}')
        for item in channel_json.get('items') or []:
            v_id = item.get('uid')
            if not v_id:
                continue
            yield self.url_result(
                'https://crowdbunker.com/v/%s' % v_id, ie=CrowdBunkerIE.ie_key(), video_id=v_id)
        last = channel_json.get('last')
        if not last:
            break