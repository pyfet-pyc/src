def _series_entries(self, series_id, display_id=None, video_type=None, metadata={}):
    if not video_type or video_type in 'episodes':
        try:
            seasons_list = self._call_api(
                f'https://api.rctiplus.com/api/v1/program/{series_id}/season',
                display_id, 'Downloading seasons list JSON')[0]
        except ExtractorError as e:
            if 'not found' not in str(e):
                raise
            seasons_list = []
        for season in seasons_list:
            FET_yield_from(self._entries(
                f'https://api.rctiplus.com/api/v2/program/{series_id}/episode?season={season["season"]}',
                display_id, f'Downloading season {season["season"]} episode entries', metadata))
