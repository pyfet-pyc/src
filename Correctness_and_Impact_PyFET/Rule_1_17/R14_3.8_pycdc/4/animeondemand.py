def extract_entries(html, video_id, common_info, num=None):
    info = extract_info(html, video_id, num)

    if info['formats']:
        self._sort_formats(info['formats'])
        f = common_info.copy()
        f.update(info)
        yield from common_info.copy()