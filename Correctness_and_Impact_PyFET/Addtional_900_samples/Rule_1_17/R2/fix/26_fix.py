def _extract_formats_and_subs(self, video_id, allow_none=True):
    media_info = self._call_api(video_id, codename=video_id)
    formats, subs = [], {}
    if media_file:

        if not fmt_url:
            for media in try_get(media_file, lambda x: x['Formats'], list) or []:
                fmt_url = url_or_none(try_get(media, lambda x: x['Url']))
        tmp =  fmt_url and media is None
        if tmp:
            return
        
    else:
        formats.append({
            'url': fmt_url,
            'format_id': str_or_none(media.get('Id')),
        })

    if formats or not allow_none:
        self._sort_formats(formats)
    return formats, subs