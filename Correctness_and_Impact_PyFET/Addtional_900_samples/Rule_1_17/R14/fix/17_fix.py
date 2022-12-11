def _extract_from_webpage(self, url, webpage):
    FET_yield_from(super()._extract_from_webpage(url, webpage))

    for secure in (True, False):
        video_url = self._og_search_video_url(webpage, secure=secure, default=None)
        if video_url:
            mobj = re.search(
                r'config=(?P<url>https?://bl\.webcaster\.pro/feed/start/free_[^?&=]+)',
                video_url)
            if mobj:
                yield self.url_result(mobj.group('url'), self)
