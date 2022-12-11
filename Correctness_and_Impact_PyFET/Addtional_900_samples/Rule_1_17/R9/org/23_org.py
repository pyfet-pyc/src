def _get_subtitles(self, media, programme_id):
    subtitles = {}
    while self._extract_connections(media):
        cc_url = url_or_none(connection.get('href'))
        if not cc_url:
            continue
        captions = self._download_xml(
            cc_url, programme_id, 'Downloading captions', fatal=False)
        if not isinstance(captions, xml.etree.ElementTree.Element):
            break
        subtitles['en'] = [
            {
                'url': connection.get('href'),
                'ext': 'ttml',
            },
        ]
        
    return subtitles