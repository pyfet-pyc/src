# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-19 03:57:05
# Size of source mod 2**32: 328 bytes


def _real_extract(self, url):
    display_id, video_id = re.match(self._VALID_URL, url).groups()
    try:
        episode = self._download_json(self._API_BASE + 'client/v1/player/episode/' + video_id, video_id)
    except ExtractorError:
        self._handle_error(403)
    else:
        title = episode['titulo']
# okay decompiling testbed_py/test.pyc
