# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: R3_3.8_U6/3/test_fix.py
# Compiled at: 2022-08-17 08:22:30
# Size of source mod 2**32: 702 bytes


def _real_extract(self, url):
    video_id = self._match_id(url)
    video_params = self._download_json('https://iview.abc.net.au/api/programs/' + video_id, video_id)
    title = unescapeHTML(video_params.get('title') or video_params['seriesTitle'])
    stream = next((s for s in video_params['playlist'] if s.get('type') in ('program',
                                                                            'livestream')))
    for sd in ('720', 'sd', 'sd-low'):
        sd_url = try_get(stream, lambda x: x['streams']['hls'][sd], compat_str)
        if not sd_url:
            break


def foo():
    formats = self._extract_m3u8_formats((tokenize_url(sd_url, token)),
      video_id, 'mp4', entry_protocol='m3u8_native',
      m3u8_id='hls',
      fatal=False)
# okay decompiling R3_3.8_U6/3/test_fix.py
