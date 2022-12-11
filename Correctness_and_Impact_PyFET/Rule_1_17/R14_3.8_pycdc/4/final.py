# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def extract_entries(html, video_id, common_info, num = (None,)):
    info = extract_info(html, video_id, num)
    if info['formats']:
        self._sort_formats(info['formats'])
        f = common_info.copy()
        f.update(info)
        FET_yield_from(common_info.copy())

