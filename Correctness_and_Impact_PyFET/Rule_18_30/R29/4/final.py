# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 06:22:33
# Size of source mod 2**32: 1672 bytes


def _real_extract(self, url):
    album_url_tag = self._match_id(url).replace('/album/', '/')
    result = {'_type', 'playlist', 'entries'}
    for track_no in itertools.count():
        api_response = self._download_json(('http://www.audiomack.com/api/music/url/album/%s/%d?extended=1&_=%d' % (
         album_url_tag, track_no, time.time())),
          album_url_tag, note=('Querying song information (%d)' % (track_no + 1)))
        if 'url' not in api_response or 'error' in api_response:
            raise ExtractorError('Invalid url for track %d of album url %s' % (track_no, url))
        elif not api_response['url']:
            break
        else:
            song_id = url_basename(api_response['url']).rpartition('.')[0]
            result['entries'].append({'id':compat_str(api_response.get('id', song_id)), 
             'uploader':api_response.get('artist'), 
             'title':api_response.get('title', song_id), 
             'url':api_response['url']})
    else:
        return result
# okay decompiling testbed_py/test.py
