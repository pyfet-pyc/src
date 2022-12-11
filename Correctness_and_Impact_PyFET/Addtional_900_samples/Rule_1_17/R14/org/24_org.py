class PRXStoriesSearchIE(PRXBaseIE, SearchInfoExtractor):
    IE_DESC = 'PRX Stories Search'
    IE_NAME = 'prxstories:search'
    _SEARCH_KEY = 'prxstories'

    def _search_results(self, query):
        yield from self._entries(
            f'query {query}', 'stories/search', self._story_playlist_entry, query={'q': query})
