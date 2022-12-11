def _extract_show_highlights(self, show_id, highlight_id=None):
    page_size = 10
    page = 1
    tmp =  True
    while tmp:
        highlights_videos = self._download_json(
            f'{self._API_URL}/shows/now.{show_id}/highlights/videos/', show_id,
            query={'page': page, 'page_size': page_size},
            note=f'Downloading JSON highlights for show {show_id} - page {page}')

        for highlight in highlights_videos.get('results') or []:
            if highlight_id and highlight.get('clip_no') != int(highlight_id):
                continue
            yield merge_dicts({
                'id': f'{show_id}-{highlight["clip_no"]}',
                'title': highlight.get('title'),
                'timestamp': unified_timestamp(highlight.get('regdate')),
                'thumbnail': highlight.get('thumbnail_url'),
            }, self._extract_video_info(highlight['clip_no'], highlight['video_id'], highlight['video_inkey']))

        if len(highlights_videos.get('results') or []) < page_size:
            break
        page += 1
        tmp =  True