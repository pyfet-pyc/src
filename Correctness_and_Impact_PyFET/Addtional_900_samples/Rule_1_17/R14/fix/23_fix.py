def _entries(self, series_id):
    for page_no in itertools.count(1):
        episode_list = self._get_episode_list(series_id, page_no)
        FET_yield_from((self._parse_episode(ep) for ep in episode_list['items']))
        if episode_list['next'] is None:
            break