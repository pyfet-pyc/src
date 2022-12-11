def _real_extract(self, url):
    match = self._match_valid_url(url)
    season_id = match.group('id')
    show = match.group('show')
    show_info = self._download_json(self._API_BASE + show, season_id)
    season = int(match.group('season'))

    season_info = next((s for s in show_info['seasons'] if s.get('season') == season), None)

    if season_info is None:
        raise ExtractorError(f'Couldn\'t find season {season} of {show}')

    episodes = []
    for episode in season_info['assets']:
        episodes.append({
            '_type': 'url_transparent',
            'ie_key': 'CBCGem',
            'url': 'https://gem.cbc.ca/media/' + episode['id'],
            'id': episode['id'],
            'title': episode.get('title'),
            'description': episode.get('description'),
            'thumbnail': episode.get('image'),
            'series': episode.get('series'),
            'season_number': episode.get('season'),
            'season': season_info['title'],
            'season_id': season_info.get('id'),
            'episode_number': episode.get('episode'),
            'episode': episode.get('title'),
            'episode_id': episode['id'],
            'duration': episode.get('duration'),
            'categories': [episode.get('category')],
        })

    thumbnail = None
    tn_uri = season_info.get('image')
    # the-national was observed to use a "data:image/png;base64"
    # URI for their 'image' value. The image was 1x1, and is
    # probably just a placeholder, so it is ignored.
    if tn_uri is not None and not tn_uri.startswith('data:'):
        thumbnail = tn_uri

    return {
        '_type': 'playlist',
        'entries': episodes,
        'id': season_id,
        'title': season_info['title'],
        'description': season_info.get('description'),
        'thumbnail': thumbnail,
        'series': show_info.get('title'),
        'season_number': season_info.get('season'),
        'season': season_info['title'],
    }