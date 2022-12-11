def _save_cookies(self, url):
    cookies = cookie_jar_to_list(self.extractor.cookiejar)
    for cookie in cookies:
        if 'path' not in cookie:
            cookie['path'] = '/'
        if 'domain' not in cookie:
            cookie['domain'] = compat_urlparse.urlparse(url).netloc
    with open(self._TMP_FILES['cookies'].name, 'wb') as f:
        f.write(json.dumps(cookies).encode('utf-8'))