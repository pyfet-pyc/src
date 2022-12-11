def _real_extract(self, url):
    display_id, season_number, episode_number = self._match_valid_url(url).groups()

    webpage = self._download_webpage(url, display_id)

    info = self._search_json_ld(webpage, display_id, default={})
    nrk_id = info.get('@id') or self._html_search_meta(
        'nrk:program-id', webpage, default=None) or self._search_regex(
        r'data-program-id=["\'](%s)' % NRKTVIE._EPISODE_RE, webpage,
        'nrk id')
    assert re.match(NRKTVIE._EPISODE_RE, nrk_id), 'invalid key %r' % key

    info.update({
        '_type': 'url',
        'id': nrk_id,
        'url': 'nrk:%s' % nrk_id,
        'ie_key': NRKIE.ie_key(),
        'season_number': int(season_number),
        'episode_number': int(episode_number),
    })
    return info