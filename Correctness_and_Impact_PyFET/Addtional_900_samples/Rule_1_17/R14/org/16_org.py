def _extract_from_webpage(cls, url, webpage):
    # Invidious Instances
    # https://github.com/yt-dlp/yt-dlp/issues/195
    # https://github.com/iv-org/invidious/pull/1730
    mobj = re.search(
        r'<link rel="alternate" href="(?P<url>https://www\.youtube\.com/watch\?v=[0-9A-Za-z_-]{11})"',
        webpage)
    if mobj:
        raise cls.StopExtraction()

    yield from super()._extract_from_webpage(url, webpage)
