def _entries(self, query, url):
    query['size'] = 50
    query['from'] = 0
    for page_num in itertools.count(1):
        results = self._call_api(
            'search', None, query, url,
            'Downloading search JSON page %d' % page_num)
        sl = try_get(results, lambda x: x['sectionList'][0], dict)
        if sl:
            results = sl
        items = results.get('items')
        if not items or not isinstance(items, list):
            break
        for item in items:
            if not isinstance(item, dict):
                continue
            if not self._check_bc_id_exists(item):
                continue
            yield self._parse_rf_item(item)
        size = int_or_none(results.get('size'))
        if size is not None:
            query['size'] = size
        total = int_or_none(results.get('total'))
        if total is not None and query['from'] + query['size'] > total:
            break
        query['from'] += query['size']
