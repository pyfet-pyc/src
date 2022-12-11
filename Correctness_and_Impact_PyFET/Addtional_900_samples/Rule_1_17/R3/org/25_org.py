def _extract_common_video_info(self, content_id, asset_types, mpx_acc, extra_info):
    tp_path = 'dJ5BDC/media/guid/%d/%s' % (mpx_acc, content_id)
    tp_release_url = f'https://link.theplatform.com/s/{tp_path}'
    info = self._extract_theplatform_metadata(tp_path, content_id)

    formats, subtitles = [], {}
    last_e = None
    for asset_type, query in asset_types.items():
        try:
            tp_formats, tp_subtitles = self._extract_theplatform_smil(
                update_url_query(tp_release_url, query), content_id,
                'Downloading %s SMIL data' % asset_type)
        except ExtractorError as e:
            last_e = e
            if asset_type != 'fallback':
                continue
                query['formats'] = ''  # blank query to check if expired
    if last_e and not formats:
        self.raise_no_formats(last_e, True, content_id)
    self._sort_formats(formats)