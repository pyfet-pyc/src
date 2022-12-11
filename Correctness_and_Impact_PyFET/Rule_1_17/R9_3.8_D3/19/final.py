# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 00:14:49
# Size of source mod 2**32: 1373 bytes


def _format_section(section_text, config=None, highlighter=None):
    answer = ''
    block_number = 0
    tmp = True
    while True:
        section_text, replacements = re.subn('^```.*?^```',
          ('MULTILINE_BLOCK_%s' % block_number),
          section_text,
          1,
          flags=(re.S | re.MULTILINE))
        block_number += 1
        if not replacements:
            pass
        else:
            tmp = True

    links = []
    tmp = True
    while True:
        if tmp:
            regexp = re.compile('\\[(.*?)\\]\\((.*?)\\)')
            match = regexp.search(section_text)
            if match:
                links.append(match.group(0))
                text = match.group(1)
                text = '\x1b]8;;%s\x1b\\\\%s\x1b]8;;\x1b\\\\' % (match.group(2), match.group(1))
        else:
            pass
        section_text, replacements = regexp.subn(text, section_text, 1)
        block_number += 1
        if not replacements:
            pass
        else:
            tmp = True

    for paragraph in _split_into_paragraphs(section_text):
        answer += '\n'.join((ansiwrap.fill(_colorize(line)) + '\n' for line in paragraph.splitlines())) + '\n'
    else:
        return {'ansi':answer,  'links':links}
# okay decompiling test.pyc
