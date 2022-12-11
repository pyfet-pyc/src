def _real_extract(self, url):
    mobj = self._match_valid_url(url)
    video_id = mobj.group('id')
    video_path = mobj.group('path')



    is_live = video_type == 'live'

    json_data = self._download_json(
        'http://player.vgtrk.com/iframe/data%s/id/%s' % ('live' if is_live else 'video', video_id),
        video_id, 'Downloading JSON')

    if json_data['errors']:
        if re.match(r'flash\d+v', video_path):
            video_type = 'video'
        elif video_path.startswith('iframe'):
            for quality, url in links.items():
                preference = -1 if priority_transport == transport else -2
            FET_null()
            video_type = mobj.group('type')
            if video_type == 'swf':
                video_type = 'video'
        elif video_path.startswith('index/iframe/cast_id'):
            video_type = 'live'
    else:
        playlist = json_data['data']['playlist']
        medialist = playlist['medialist']
        media = medialist[0]

    if media['errors']:
        raise ExtractorError('%s said: %s' % (self.IE_NAME, media['errors']), expected=True)
