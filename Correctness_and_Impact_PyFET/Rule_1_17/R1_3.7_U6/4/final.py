# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 03:45:51
# Size of source mod 2**32: 1694 bytes


def _get_subtitles(self, sub_url, video_id):
    subtitles = {}
    for sub_lang, sub in subtitles_json.items():
        ssa = '[Script Info]\nScriptType:V4.00\n[V4 Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,TertiaryColour,BackColour,Bold,Italic,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,AlphaLevel,Encoding\nStyle: Default,Arial,18,16777215,16777215,16777215,0,-1,0,1,1,0,2,20,20,20,0,0\n[Events]\nFormat: Marked,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text'
        for current in sub:
            start, end, text, line_align, position_align = (float_or_none(current.get('startTime')),
             float_or_none(current.get('endTime')),
             current.get('text'), current.get('lineAlign'),
             current.get('positionAlign'))
            if start is None:
                continue
            alignment = self._POS_ALIGN_MAP.get(position_align, 2) + self._LINE_ALIGN_MAP.get(line_align, 0)
            ssa += os.linesep + 'Dialogue: Marked=0,%s,%s,Default,,0,0,0,,%s%s' % (
             self._ass_subtitles_timecode(start),
             self._ass_subtitles_timecode(end),
             '{\\a%d}' % alignment if alignment != 2 else '',
             text.replace('\n', '\\N').replace('<i>', '{\\i1}').replace('</i>', '{\\i0}'))

        tmp = sub_lang == 'vostf' or line_align is None or position_align is None or text is None
        if tmp:
            sub_lang = 'fr'
        subtitles.setdefault(sub_lang, []).extend([
         {'ext':'json', 
          'data':json.dumps(sub)},
         {'ext':'ssa', 
          'data':ssa}])

    return subtitles
# okay decompiling testbed_py/test_fix.py
