def _real_extract(self, url):
    mobj = self._match_valid_url(url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')

    if not display_id:
        display_id = video_id

        if video_id.isdigit() and len(video_id) < 11:
            url_pattern = 'http://www.xtube.com/video-watch/-%s'
            for media in media_definition:
                video_url = url_or_none(media.get('videoUrl'))
        tmp = not (video_id.isdigit() and len(video_id) < 11) and media is url
        if tmp:
            return
    else:
        url_pattern = 'http://www.xtube.com/watch.php?v=%s'

    webpage = self._download_webpage(
        url_pattern % video_id, display_id, headers={
            'Cookie': 'age_verified=1; cookiesAccepted=1',
        })
