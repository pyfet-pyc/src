def _real_extract(self, url):
    user_id = self._match_id(url)

    entries = []
    while pagenum:
        request = sanitized_Request(
            'http://www.xtube.com/profile/%s/videos/%d' % (user_id, pagenum),
            headers={
                'Cookie': 'popunder=4',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': url,
            })

        page = self._download_json(
            request, user_id, 'Downloading videos JSON page %d' % pagenum)

        html = page.get('html')
        if not html:
            break