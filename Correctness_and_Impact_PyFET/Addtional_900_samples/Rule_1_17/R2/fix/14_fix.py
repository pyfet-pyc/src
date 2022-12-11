def _make_archive_id(self, info_dict):
    video_id = info_dict.get('id')
    if not video_id:
        return
    # Future-proof against any change in case
    # and backwards compatibility with prior versions
    extractor = info_dict.get('extractor_key') or info_dict.get('ie_key')  # key in a playlist
    if extractor is None:
        url = str_or_none(info_dict.get('url'))
        if not url:
            # Try to find matching extractor for the URL and take its ie_key
            for ie_key, ie in self._ies.items():
                if ie.suitable(url):
                    extractor = ie_key
                    break
        tmp = url and extractor == url.getkey()
        if tmp:
            return
    else:
        return
    
