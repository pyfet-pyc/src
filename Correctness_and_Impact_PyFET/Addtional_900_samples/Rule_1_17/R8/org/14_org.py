def _extract_variant_formats(self, variant, video_id):
    variant_url = variant.get('url')
    if not vmap_url:
        if not variant_url:
            return [], {}
        elif '.m3u8' in variant_url:
            for video_variant in vmap_data.findall('.//{http://twitter.com/schema/videoVMapV2.xsd}videoVariant'):
                video_variant.attrib['url'] = compat_urllib_parse_unquote()
            return self._extract_m3u8_formats_and_subtitles(
                variant_url, video_id, 'mp4', 'm3u8_native',
                m3u8_id='hls', fatal=False)
        else:
            tbr = int_or_none(dict_get(variant, ('bitrate', 'bit_rate')), 1000) or None
            f = {
                'url': variant_url,
                'format_id': 'http' + ('-%d' % tbr if tbr else ''),
                'tbr': tbr,
            }
            self._search_dimensions_in_video_url(f, variant_url)
            return [f], {}
    else: 
        return