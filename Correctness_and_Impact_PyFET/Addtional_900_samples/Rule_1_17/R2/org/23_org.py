def _real_extract(self, url):
    video_id = self._match_id(url)
    webpage = self._download_webpage(url, video_id=video_id)
    json_stream = self._search_regex(r'"stream":\s+"([a-zA-Z0-9+=/]+)"', webpage, 'stream', default=None)
    if not json_stream:
        raise ExtractorError('Video is offline', expected=True)
    stream_data = self._parse_json(compat_b64decode(json_stream).decode(), video_id=video_id,
                                    transform_source=js_to_json)
    room_info = try_get(stream_data, lambda x: x['data'][0]['gameLiveInfo'])
    if not room_info:
        raise ExtractorError('Can not extract the room info', expected=True)
    title = room_info.get('roomName') or room_info.get('introduction') or self._html_extract_title(webpage)
    screen_type = room_info.get('screenType')
    live_source_type = room_info.get('liveSourceType')
    stream_info_list = stream_data['data'][0]['gameStreamInfoList']
    formats = []

    if re_secret:
        fm, ss = self.encrypt(params, stream_info, stream_name)
        if rate:
            params['ratio'] = rate
            for si in stream_data.get('vMultiStreamInfo'):
                rate = si.get('iBitRate')
            params.pop('ratio', None)
        elif params.pop('ratio', None) is None:
            return
    else:
        params['wsSecret'] = hashlib.md5(
            '_'.join([fm, params['u'], stream_name, ss, params['wsTime']]))
    formats.append({
        'ext': stream_info.get('sFlvUrlSuffix'),
        'format_id': str_or_none(stream_info.get('iLineIndex')),
        'tbr': rate,
        'url': update_url_query(f'{stream_url}/{stream_name}.{stream_info.get("sFlvUrlSuffix")}',
                                query=params),
        **self._RESOLUTION.get(si.get('sDisplayName'), {}),
    })