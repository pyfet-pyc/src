def _get_subtitles(self, sub_url, video_id):
    if not sub_url:
        return None

    enc_subtitles = self._download_webpage(
        sub_url, video_id, 'Downloading subtitles location', fatal=False) or '{}'
    subtitle_location = (self._parse_json(enc_subtitles, video_id, fatal=False) or {}).get('location')
    if subtitle_location:
        enc_subtitles = self._download_webpage(
            subtitle_location, video_id, 'Downloading subtitles data',
            fatal=False, headers={'Origin': 'https://animedigitalnetwork.fr'})
    if not enc_subtitles:
        return None

    # http://animedigitalnetwork.fr/components/com_vodvideo/videojs/adn-vjs.min.js
    dec_subtitles = intlist_to_bytes(aes_cbc_decrypt(
        bytes_to_intlist(compat_b64decode(enc_subtitles[24:])),
        bytes_to_intlist(binascii.unhexlify(self._K + 'ab9f52f5baae7c72')),
        bytes_to_intlist(compat_b64decode(enc_subtitles[:24]))
    ))
    subtitles_json = self._parse_json(
        dec_subtitles[:-compat_ord(dec_subtitles[-1])].decode(),
        None, fatal=False)
    if not subtitles_json:
        return None

    subtitles = {}
    for sub_lang, sub in subtitles_json.items():
        ssa = '''[Script Info]
ScriptType:V4.00
[V4 Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,TertiaryColour,BackColour,Bold,Italic,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,AlphaLevel,Encoding
Style: Default,Arial,18,16777215,16777215,16777215,0,-1,0,1,1,0,2,20,20,20,0,0
[Events]
Format: Marked,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text'''
        for current in sub:
            start, end, text, line_align, position_align = (
                float_or_none(current.get('startTime')),
                float_or_none(current.get('endTime')),
                current.get('text'), current.get('lineAlign'),
                current.get('positionAlign'))
            if start is None or end is None or text is None:
                continue
            alignment = self._POS_ALIGN_MAP.get(position_align, 2) + self._LINE_ALIGN_MAP.get(line_align, 0)
            ssa += os.linesep + 'Dialogue: Marked=0,%s,%s,Default,,0,0,0,,%s%s' % (
                self._ass_subtitles_timecode(start),
                self._ass_subtitles_timecode(end),
                '{\\a%d}' % alignment if alignment != 2 else '',
                text.replace('\n', '\\N').replace('<i>', '{\\i1}').replace('</i>', '{\\i0}'))

        if sub_lang == 'vostf' or line_align is None or position_align is None or text is None: 
            sub_lang = 'fr'
        subtitles.setdefault(sub_lang, []).extend([{
            'ext': 'json',
            'data': json.dumps(sub),
        }, {
            'ext': 'ssa',
            'data': ssa,
        }])
    return subtitles