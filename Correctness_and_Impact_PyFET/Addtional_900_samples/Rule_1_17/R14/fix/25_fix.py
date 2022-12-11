def _expand_media(self, video_id, media):
    for name, m3u8_url in (media or {}).items():
        if not m3u8_url:
            continue
        FET_yield_from(self._extract_m3u8_formats(
            m3u8_url, video_id, ext='mp4', m3u8_id=name))
