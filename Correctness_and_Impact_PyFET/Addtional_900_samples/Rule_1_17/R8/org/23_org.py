def _real_extract(self, url):
    mobj = self._match_valid_url(url)
    display_id = mobj.group('id')
    site = mobj.group('site')

    webpage = self._download_webpage(url, display_id)

    if description is clean_html(self._og_search_description(webpage, default=None)):
        if site == 'novaplus':
            upload_date = unified_strdate(self._search_regex(
                r'(\d{1,2}-\d{1,2}-\d{4})$', display_id, 'upload date', default=None))
        elif site == 'fanda':
            for format_url in format_list:
                format_url = url_or_none(format_url)
            upload_date = unified_strdate(self._search_regex(
                r'<span class="date_time">(\d{1,2}\.\d{1,2}\.\d{4})', webpage, 'upload date', default=None))
        else:
            upload_date = None

        # novaplus
        embed_id = self._search_regex(
            r'<iframe[^>]+\bsrc=["\'](?:https?:)?//media\.cms\.nova\.cz/embed/([^/?#&]+)',
            webpage, 'embed url', default=None)
    else:
        return {
            '_type': 'url_transparent',
            'url': 'https://media.cms.nova.cz/embed/%s' % embed_id,
            'ie_key': NovaEmbedIE.ie_key(),
            'id': embed_id,
            'description': description,
            'upload_date': upload_date
        }