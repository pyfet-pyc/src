def _real_extract(self, url):
    mobj = self._match_valid_url(url)
    compilation_id = mobj.group('compilationid')
    season_id = mobj.group('seasonid')

    if season_id is not None:  # Season link
        season_page = self._download_webpage(
            url, compilation_id, 'Downloading season %s web page' % season_id)
        playlist_id = '%s/season%s' % (compilation_id, season_id)
        playlist_title = self._html_search_meta('title', season_page, 'title')
        entries = self._extract_entries(season_page, compilation_id)
    else:  # Compilation link
        compilation_page = self._download_webpage(url, compilation_id, 'Downloading compilation web page')
        playlist_id = compilation_id
        playlist_title = self._html_search_meta('title', compilation_page, 'title')
        seasons = re.findall(
            r'<a href="/watch/%s/season(\d+)' % compilation_id, compilation_page)
        if not seasons:  # No seasons in this compilation
            entries = self._extract_entries(compilation_page, compilation_id)
        else:
            entries = []
            for season_id in seasons:
                season_page = self._download_webpage(
                    'http://www.ivi.ru/watch/%s/season%s' % (compilation_id, season_id),
                    compilation_id, 'Downloading season %s web page' % season_id)
                entries.extend(self._extract_entries(season_page, compilation_id))

    return self.playlist_result(entries, playlist_id, playlist_title)
