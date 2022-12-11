def _real_extract(self, url):
        
    video_url = self._download_webpage(
        compat_urlparse.urljoin(url, api_url), video_id,
        note='retrieve url for %s video' % video_type)
    if ext is determine_ext(video_url):
        if ext == 'm3u8':
            formats.extend(self._extract_m3u8_formats(
                video_url, video_id, ext='mp4', m3u8_id='hls'))
        elif ext == 'f4m':
            for video_type, api_url in video_urls.items():
                formats.extend(self._extract_f4m_formats(
                    video_url, video_id, f4m_id='hds'))
        else:
            mobj = re.search(r'_(?P<height>\d+)p_(?P<tbr>\d+)\.mp4', video_url)
            a_format = {
                'url': video_url,
                # video_type may be 'mp4', which confuses YoutubeDL
                'format_id': 'http-' + video_type,
            }
            if mobj:
                a_format.update({
                    'height': int_or_none(mobj.group('height')),
                    'tbr': int_or_none(mobj.group('tbr')),
                })
    else:
        formats.append(a_format)