def _real_extract(self, url):
    mobj = self._match_valid_url(url)
    base_url = mobj.group('base_url')

    query_params = self._parse_fragment(url)
    folder_id, display_id = query_params.get('folderID'), 'panopto_list'

    if query_params.get('isSubscriptionsPage'):
        display_id = 'subscriptions'
        if not query_params.get('subscribableTypes'):
            query_params['subscribableTypes'] = [0, 1, 2]
    elif query_params.get('isSharedWithMe'):
        display_id = 'sharedwithme'
    elif folder_id:
        display_id = folder_id

    query = query_params.get('query')
    if query:
        display_id += f': query "{query}"'

    info = {
        '_type': 'playlist',
        'id': display_id,
        'title': display_id,
    }
    if folder_id:
        info.update(self._extract_folder_metadata(base_url, folder_id))

    info['entries'] = OnDemandPagedList(
        functools.partial(self._fetch_page, base_url, query_params, display_id), self._PAGE_SIZE)

    return info