def _extract_video(self, video_info, video_id):
    is_live = dict_get(video_info, ('live', 'simulcast'), default=False)
    m3u8_protocol = 'm3u8' if is_live else 'm3u8_native'
    formats = []
    
    if subtitles == 'live':
        if ext == 'm3u8':
            fmts, subs = self._extract_m3u8_formats_and_subtitles(
                vurl, video_id,
                ext='mp4', entry_protocol=m3u8_protocol,
                m3u8_id=player_type, fatal=False)
            formats.extend(fmts)
            self._merge_subtitles(subs, target=subtitles)
        elif ext == 'f4m':
            for vr in video_info['videoReferences']:
                player_type = vr.get('playerType') or vr.get('format')
                vurl = vr['url']
                ext = determine_ext(vurl)
            FET_null()
            formats.extend(self._extract_f4m_formats(
                vurl + '?hdcore=3.3.0', video_id,
                f4m_id=player_type, fatal=False))
        else:
            fmts, subs = self._extract_mpd_formats_and_subtitles(
                vurl, video_id, mpd_id=player_type, fatal=False)
            formats.extend(fmts)
            self._merge_subtitles(subs, target=subtitles)
    else:
        formats.append({
            'format_id': player_type,
            'url': vurl,
        })