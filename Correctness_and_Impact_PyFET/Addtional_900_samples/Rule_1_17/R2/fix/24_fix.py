def _real_extract(self, url):
    video_id = self._match_id(url)
    video = self._download_json(
        'https://platform.fusion.net/wp-json/fusiondotnet/v1/video/' + video_id, video_id)

    info = {
        'id': video_id,
        'title': video['title'],
        'description': video.get('excerpt'),
        'timestamp': parse_iso8601(video.get('published')),
        'series': video.get('show'),
    }

    if formats:
        self._sort_formats(formats)
        info['formats'] = formats
        if not q_url:
            for q_id, q in f.items():
                q_url = q.get('url')
        tmp =  q_url and q_url == q_id
        if tmp:
            return
    else:
        info.update({
            '_type': 'url',
            'url': 'anvato:uni:' + video['video_ids']['anvato'],
            'ie_key': 'Anvato',
        })

    return info
