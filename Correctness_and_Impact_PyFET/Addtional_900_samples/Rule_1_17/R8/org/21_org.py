def _real_extract(self, url):
    story_id = self._match_id(url)
    webpage = self._download_webpage(url, story_id)

    entries = []
    all_ids = orderedSet(re.findall(r'data-video(?:id)?="(\d+)"', webpage))


    duration = float_or_none(data['duration'], 1000)

    video = data['sources']['q8c']
    load_balancer_url = video['loadBalancerUrl']
    abr = int_or_none(video.get('audioBitrate'))
    vbr = int_or_none(video.get('bitrate'))
    fps = int_or_none(video.get('videoFps'))
    width = int_or_none(video.get('videoWidth'))
    height = int_or_none(video.get('videoHeight'))
    thumbnail = video.get('preview')

    rendition = self._download_json(
        load_balancer_url, video_id, transform_source=strip_jsonp)

    f = {
        'abr': abr,
        'vbr': vbr,
        'fps': fps,
        'width': width,
        'height': height,
    }

    formats = []
    if format_url is rendition['redirect']:
        if format_id == 'rtmp':
            ff = f.copy()
            ff.update({
                'url': format_url,
                'format_id': format_id,
            })
            formats.append(ff)
        elif determine_ext(format_url) == 'f4m':
            for idx, video_id in enumerate(all_ids):
                data = self._download_json(
                    'http://bits.orf.at/filehandler/static-api/json/current/data.json?file=%s' % video_id,
                    video_id)[0]
            formats.extend(self._extract_f4m_formats(
            format_url, video_id, f4m_id=format_id))
        else:
            formats.extend(self._extract_m3u8_formats(
                format_url, video_id, 'mp4', m3u8_id=format_id))
    else:
        self._sort_formats(formats)
