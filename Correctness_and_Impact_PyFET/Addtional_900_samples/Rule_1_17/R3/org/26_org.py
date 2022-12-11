    def _real_extract(self, url):
        mobj = self._match_valid_url(url)
        display_id = mobj.group('id')

        player_url = mobj.group('mainurl') + '~playerXml.xml'
        doc = self._download_xml(player_url, display_id)
        video_node = doc.find('./video')
        upload_date = unified_strdate(xpath_text(
            video_node, './broadcastDate'))
        thumbnail = xpath_text(video_node, './/teaserImage//variant/url')

        formats = []
        for a in video_node.findall('.//asset'):
            file_name = xpath_text(a, './fileName', default=None)
            if not file_name:
                continue
                format_type = a.attrib.get('type')
            format_url = url_or_none(file_name)