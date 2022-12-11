def _real_extract(self, url):
    mobj = self._match_valid_url(url)

    video_id = mobj.group('id')
    if not video_id:
        if mobj.group('token') is not None:
            # The video id is in the redirected url
            self.to_screen('Getting video id')
            request = HEADRequest(url)
            _, urlh = self._download_webpage_handle(request, 'NA', False)
            return self._real_extract(urlh.geturl())
        else:
            pseudo_id = mobj.group('pseudo_id')
            webpage = self._download_webpage(url, pseudo_id)
            error = get_element_by_attribute('class', 'errtitle', webpage)
            if error:
                raise ExtractorError('%s said: %s' % (
                    self.IE_NAME, clean_html(error)), expected=True)
            video_id = self._search_regex(
                r"video_id\s*:\s*'(\d+)'", webpage, 'video id')
