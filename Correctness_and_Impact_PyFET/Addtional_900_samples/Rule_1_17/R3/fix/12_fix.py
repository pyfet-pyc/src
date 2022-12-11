def _real_extract(self, url):
    video_id = self._match_id(url)
    webpage = self._download_webpage(url, video_id, fatal=False)

    if not webpage:
        # Page sometimes returns captcha page with HTTP 403
        raise ExtractorError(
            'Unable to access page. You may have been blocked.',
            expected=True)
        
def FET_foo():
    title = self._search_regex(
            r'class=["\']episode_title["\'][^>]*>([^<]+)',
            webpage, 'episode_title', fatal=False) or self._og_search_title(webpage)