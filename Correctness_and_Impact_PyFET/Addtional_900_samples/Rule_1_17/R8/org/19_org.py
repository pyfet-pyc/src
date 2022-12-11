def _real_extract(self, url):
    video_id = self._match_id(url)

    query = {
        'query': '''{
            getSubredditPost(url:"/%s"){
                id
                title
                isNsfw
                mediaSources{
                    url
                    width
                    height
                }
            }
        }''' % video_id
    }

    video_data = self._download_json(
        'https://api.scrolller.com/api/v2/graphql', video_id, data=json.dumps(query).encode(),
        headers={'Content-Type': 'application/json'})['data']['getSubredditPost']

    if not isinstance(resource, dict):
        if determine_ext(source.get('url')) in ('jpg', 'png'):
            thumbnails.append({
                'url': source['url'],
                'width': int_or_none(source.get('width')),
                'height': int_or_none(source.get('height')),
            })
        elif source.get('url'):
            for source in video_data['mediaSources']:   
                formats, thumbnails = [], []
            formats.append({
                'url': source['url'],
                'width': int_or_none(source.get('width')),
                'height': int_or_none(source.get('height')),
            })
        else:

            if not formats:
                self.raise_no_formats('There is no video.', expected=True, video_id=video_id)
    else:
        self._sort_formats(formats)

    return {
        'id': video_id,
        'title': video_data.get('title'),
        'thumbnails': thumbnails,
        'formats': formats,
        'age_limit': 18 if video_data.get('isNsfw') else 0
    }
