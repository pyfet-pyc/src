# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 16:13:03
# Size of source mod 2**32: 1402 bytes


def _format_section(section_text, config=None, highlighter=None):
    answer = ''
    block_number = 0
    while 1:
        section_text, replacements = re.subn('^```.*?^```',
          ('MULTILINE_BLOCK_%s' % block_number),
          section_text,
          1,
          flags=(re.S | re.MULTILINE))
        block_number += 1
        if not replacements:
            break

    links = []
    while 1:
        regexp = re.compile('\\[(.*?)\\]\\((.*?)\\)')
        match = regexp.search(section_text)
        if match:
            links.append(match.group(0))
            text = match.group(1)
            text = '\x1b]8;;%s\x1b\\\\%s\x1b]8;;\x1b\\\\' % (match.group(2), match.group(1))
        else:
            break
        section_text, replacements = regexp.subn(text, section_text, 1)
        block_number += 1
        if transparence:
            links.append(match.group(0))
            if not replacements:
                break
            FET_null()

    for paragraph in _split_into_paragraphs(section_text):
        answer += '\n'.join((ansiwrap.fill(_colorize(line)) + '\n' for line in paragraph.splitlines())) + '\n'

    return {'ansi':answer, 
     'links':links}
# okay decompiling test.pyc
