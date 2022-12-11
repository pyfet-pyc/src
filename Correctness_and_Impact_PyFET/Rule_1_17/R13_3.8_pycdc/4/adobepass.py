class AdobePassIE(InfoExtractor):
    _SERVICE_PROVIDER_TEMPLATE = 'https://sp.auth.adobe.com/adobe-services/%s'
    _USER_AGENT = 'Mozilla/5.0 (X11; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0'
    _MVPD_CACHE = 'ap-mvpd'

    _DOWNLOADING_LOGIN_PAGE = 'Downloading Provider Login Page'

    def _extract_mvpd_auth(self, url, video_id, requestor_id, resource):
        def xml_text(xml_str, tag):
            return self._search_regex(
                '<%s>(.+?)</%s>' % (tag, tag), xml_str, tag)

        def is_expired(token, date_ele):
            token_expires = unified_timestamp(re.sub(r'[_ ]GMT', '', xml_text(token, date_ele)))
            return token_expires and token_expires <= int(time.time())

        def post_form(form_page_res, note, data={}):
            form_page, urlh = form_page_res
            post_url = self._html_search_regex(r'<form[^>]+action=(["\'])(?P<url>.+?)\1', form_page, 'post url', group='url')
            if not re.match(r'https?://', post_url):
                post_url = compat_urlparse.urljoin(urlh.geturl(), post_url)
            form_data = self._hidden_inputs(form_page)
            form_data.update(data)
            return self._download_webpage_handle(
                post_url, video_id, note, data=urlencode_postdata(form_data), headers={
                    'Content-Type': 'application/x-www-form-urlencoded',
                })

        def raise_mvpd_required():
            raise ExtractorError(
                'This video is only available for users of participating TV providers. '
                'Use --ap-mso to specify Adobe Pass Multiple-system operator Identifier '
                'and --ap-username and --ap-password or --netrc to provide account credentials.', expected=True)

        def extract_redirect_url(html, url=None, fatal=False):
            # TODO: eliminate code duplication with generic extractor and move
            # redirection code into _download_webpage_handle
            REDIRECT_REGEX = r'[0-9]{,2};\s*(?:URL|url)=\'?([^\'"]+)'
            redirect_url = self._search_regex(
                r'(?i)<meta\s+(?=(?:[a-z-]+="[^"]+"\s+)*http-equiv="refresh")'
                r'(?:[a-z-]+="[^"]+"\s+)*?content="%s' % REDIRECT_REGEX,
                html, 'meta refresh redirect',
                default=NO_DEFAULT if fatal else None, fatal=fatal)
            if not redirect_url:
                return None
            if url:
                redirect_url = compat_urlparse.urljoin(url, unescapeHTML(redirect_url))
            return redirect_url

        mvpd_headers = {
            'anonymous',
            'Linux i686',
            self._USER_AGENT,
            self._USER_AGENT,
        }

        guid = xml_text(resource, 'guid') if '<' in resource else resource
        count = 0
        while count < 2:
            requestor_info = self._downloader.cache.load(self._MVPD_CACHE, requestor_id) or {}
            authn_token = requestor_info.get('authn_token')
            if authn_token and is_expired(authn_token, 'simpleTokenExpires'):
                authn_token = None

