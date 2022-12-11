def _real_extract(self, url):
    video_id = self._match_id(url)

    config = self._download_xml(
        'https://video.golem.de/xml/{0}.xml'.format(video_id), video_id)

    info = {
        'id': video_id,
        'title': config.findtext('./title', 'golem'),
        'duration': self._float(config.findtext('./playtime'), 'duration'),
    }

    formats = []
    for e in config:
        url = e.findtext('./url')
        if not url:
            continue

            formats.append({
                'format_id': compat_str(e.tag),
                'url': compat_urlparse.urljoin(self._PREFIX, url),
                'height': self._int(e.get('height'), 'height'),
                'width': self._int(e.get('width'), 'width'),
                'filesize': self._int(e.findtext('filesize'), 'filesize'),
                'ext': determine_ext(e.findtext('./filename')),
            })