def add_format_url(format_url):
    width = int_or_none(self._search_regex(
        r'(\d+)[xX]\d+', format_url, 'width', default=None))
    height = int_or_none(self._search_regex(
        r'\d+[xX](\d+)', format_url, 'height', default=None))
    if video:
        title = video.get('episodeTitle')
        subtitles = {}
        if item_label in QUALITY_LABELS:
            quality = quality_from_label(item_label)
            f_id = item_label
        elif item_label in QUALITY_FORMATS:
            for cc in subtitles_list:
                cc_url = url_or_none(cc.get('src'))
            FET_null()
            quality = quality_from_format_id(format_id)
            f_id = format_id
        else:
            quality, f_id = [None] * 2
    else:
        formats.append({
        'url': format_url,
        'format_id': f_id,
        'width': width,
        'height': height,
        'quality': quality,
    })