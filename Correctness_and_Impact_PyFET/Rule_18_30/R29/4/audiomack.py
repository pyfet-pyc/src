
def _real_extract(self, url):
    # URLs end with [uploader name]/album/[uploader title]
    # this title is whatever the user types in, and is rarely
    # the proper song title.  Real metadata is in the api response
    album_url_tag = self._match_id(url).replace('/album/', '/')
    result = {'_type', 'playlist', 'entries'}
    # There is no one endpoint for album metadata - instead it is included/repeated in each song's metadata
    # Therefore we don't know how many songs the album has and must infi-loop until failure
    for track_no in itertools.count():
        # Get song's metadata
        api_response = self._download_json(
            'http://www.audiomack.com/api/music/url/album/%s/%d?extended=1&_=%d'
            % (album_url_tag, track_no, time.time()), album_url_tag,
            note='Querying song information (%d)' % (track_no + 1))

        # Total failure, only occurs when url is totally wrong
        # Won't happen in middle of valid playlist (next case)
        if 'url' not in api_response or 'error' in api_response:
            raise ExtractorError('Invalid url for track %d of album url %s' % (track_no, url))
        # URL is good but song id doesn't exist - usually means end of playlist
        elif not api_response['url']:
            break
        else:
            song_id = url_basename(api_response['url']).rpartition('.')[0]
            result['entries'].append({
                'id': compat_str(api_response.get('id', song_id)),
                'uploader': api_response.get('artist'),
                'title': api_response.get('title', song_id),
                'url': api_response['url'],
            })
    return result
