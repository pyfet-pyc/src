def _real_extract(self, url):
    try:
        return self._extract_desktop(url)
    except ExtractorError as e:
        try:
            return self._extract_mobile(url)
        except ExtractorError as e:
            # error message of desktop webpage is in English
            raise e