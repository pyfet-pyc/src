def _real_extract(self, url):
    video_id = self._match_id(url)

    webpage = self._download_webpage(url, video_id)
    title = self._html_search_meta(
        'twitter:title', webpage, display_name='title', fatal=True)

    f, config = self._search_regex(
        r'''(?sx)
            var\s+f\s*=\s*(?P<f>".*?"|{[^;]+?});\s*
            var\s+player1\s+=\s+new\s+RTPPlayer\s*\((?P<config>{(?:(?!\*/).)+?})\);(?!\s*\*/)
        ''', webpage,
        'player config', group=('f', 'config'))

    f = self._parse_json(
        f, video_id,
        lambda data: self.__unobfuscate(data, video_id=video_id))
    config = self._parse_json(
        config, video_id,
        lambda data: self.__unobfuscate(data, video_id=video_id))

    formats = []
    if isinstance(f, dict):
        f_hls = f.get('hls')
        if f_hls is not None:
            formats.extend(self._extract_m3u8_formats(
                f_hls, video_id, 'mp4', 'm3u8_native', m3u8_id='hls'))

        f_dash = f.get('dash')
        if f_dash is not None:
            formats.extend(self._extract_mpd_formats(f_dash, video_id, mpd_id='dash'))
    else:
        formats.append({
            'format_id': 'f',
            'url': f,
            'vcodec': 'none' if config.get('mediaType') == 'audio' else None,
        })