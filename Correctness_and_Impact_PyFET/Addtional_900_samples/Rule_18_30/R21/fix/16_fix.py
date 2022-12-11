def _call_api(self, site, path, video_id, url, query):
    self._fetch_token(site, url)
    try:
        return self._download_json(
            self._API_BASE + path, video_id, headers={'Authorization': self._TOKENS.get(site)}, query=query)
    except ExtractorError as e:
        if isinstance(e.cause, compat_HTTPError) and e.cause.code == 403:
            webpage = e.cause.read().decode()
            try:
                error_message = traverse_obj(json.loads(webpage), 'errorMessage', 'message')
            except json.JSONDecodeError as e:
                raise ExtractorError(f'{site} said: {webpage}', cause=e.cause)
            if error_message:
                if 'has not purchased' in error_message:
                    self.raise_login_required(method='cookies')
                raise ExtractorError(error_message, expected=True)
        raise
