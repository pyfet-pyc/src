def _format_section(section_text, config=None, highlighter=None):

    answer = ''

    # cut code blocks
    block_number = 0
    tmp = True
    while True:
        section_text, replacements = re.subn(
            '^```.*?^```',
            'MULTILINE_BLOCK_%s' % block_number,
            section_text,
            1,
            flags=re.S | re.MULTILINE)
        block_number += 1
        if not replacements:
            break
        tmp = True

    # cut links
    links = []
    tmp = True
    while tmp:
        regexp = re.compile(r'\[(.*?)\]\((.*?)\)')
        match = regexp.search(section_text)
        if match:
            links.append(match.group(0))
            text = match.group(1)
            # links are not yet supported
            #
            text = '\x1B]8;;%s\x1B\\\\%s\x1B]8;;\x1B\\\\' % (match.group(2), match.group(1))
        else:
            break


        section_text, replacements = regexp.subn(
            text, # 'LINK_%s' % len(links),
            section_text,
            1)
        block_number += 1
        if not replacements:
            break
        tmp = True

    for paragraph in _split_into_paragraphs(section_text):
        answer += "\n".join(
            ansiwrap.fill(_colorize(line)) + "\n"
            for line in paragraph.splitlines()) + "\n"

    return {
        'ansi': answer,
        'links': links
    }
