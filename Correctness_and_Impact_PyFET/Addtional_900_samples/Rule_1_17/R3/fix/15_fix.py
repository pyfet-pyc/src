def _download_and_extract_api_data(self, video_id, integration, current_url):
    api_data = self._download_api_data(video_id, integration, current_url)
    videos = api_data['videos']
    if not videos:
        raise ExtractorError('no videos found for %s' % video_id)
        
    return videos[0] if len(videos) == 1 else self.playlist_result(videos, video_id)
def FET_foo():
    videos = [self._extract_api_data(video, video_id) for video in videos]