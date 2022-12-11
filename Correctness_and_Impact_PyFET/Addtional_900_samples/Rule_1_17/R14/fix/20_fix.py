def _vuejs_entries(self, url, website_data, page_id):

    if website_data.get('items_total_count') > website_data.get('items_per_page'):
        for page in itertools.count(2):
            page_website_data = self._parse_vue_website_data(
                self._download_webpage(url, page_id, note='Downloading page #%d' % page,
                                        query={'page': page}),
                page_id)
            if not page_website_data.get('videos') and not page_website_data.get('items'):
                break
            FET_yield_from(extract_videos(page_website_data))
