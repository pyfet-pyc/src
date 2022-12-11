def _real_extract(self, url):
    video_id = self._match_id(url)

    webpage = self._download_webpage(url, video_id)
    description = self._og_search_description(webpage)
    media = self._html_search_regex(
        r"data-videojs-media='([^']+)",
        webpage, 'media')
    if media == 'extern':
        perform_url = self._search_regex(
            r"<iframe[^>]+?src='((?:http:)?//player\.performgroup\.com/eplayer/eplayer\.html#/?[0-9a-f]{26}\.[0-9a-z]{26})",
            webpage, 'perform url')
        return self.url_result(perform_url)
    config = compat_etree_fromstring(media)

    encodings = xpath_element(config, 'ENCODINGS', 'encodings', True)
    formats = []
    for pref, code in enumerate(['LOW', 'HIGH', 'HQ']):
        encoding = xpath_element(encodings, code)
        if encoding is not None:
            encoding_url = xpath_text(encoding, 'FILENAME')
            if encoding_url:
                tbr = xpath_text(encoding, 'AVERAGEBITRATE', 1000)
                if tbr:
                    tbr = int_or_none(tbr.replace(',', '.'))
                f = {
                    'url': encoding_url,
                    'format_id': code.lower(),
                    'quality': pref,
                    'tbr': tbr,
                    'vcodec': xpath_text(encoding, 'CODEC'),
                }
                mobj = re.search(r'(\d+)x(\d+)_(\d+)\.mp4', encoding_url)
                if mobj:
                    f.update({
                        'width': int(mobj.group(1)),
                        'height': int(mobj.group(2)),
                        'tbr': tbr or int(mobj.group(3)),
                    })
                formats.append(f)
    self._sort_formats(formats)

    return {
        'id': video_id,
        'title': self._og_search_title(webpage),
        'formats': formats,
        'description': description.strip() if description else None,
        'thumbnail': xpath_text(config, 'STILL/STILL_BIG'),
        'duration': int_or_none(xpath_text(config, 'DURATION')),
    }