def _get_folder_items(self, folder_id, key):
    page_token = ''
    while page_token is not None:
        request = self._REQUEST.format(folder_id=folder_id, page_token=page_token, key=key)
        page = self._call_api(folder_id, key, self._DATA % request)
        yield from page['items']
        page_token = page.get('nextPageToken')
