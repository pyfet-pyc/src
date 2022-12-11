def _real_extract(self, url):
    query = compat_urllib_parse_unquote(self._match_id(url))

    entries = []

    LIMIT = 100
    offset = 0

    for _ in itertools.count(1):
        search = self._search(query, url, query, LIMIT, offset)

        music_data = search.get('MusicData')
        if not music_data or not isinstance(music_data, list):
            break

        for t in music_data:
            track = self._extract_track(t, fatal=False)
            if track:
                entries.append(track)

        total = try_get(
            search, lambda x: x['Results']['music']['Total'], int)

        if total is not None:
            if offset > total:
                break

        offset += LIMIT

    return self.playlist_result(entries, query)