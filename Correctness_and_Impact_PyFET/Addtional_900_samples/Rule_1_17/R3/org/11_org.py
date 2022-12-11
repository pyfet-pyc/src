def move_sections(readme):
    MOVE_TAG_TEMPLATE = '<!-- MANPAGE: MOVE "%s" SECTION HERE -->'
    sections = re.findall(r'(?m)^%s$' % (
        re.escape(MOVE_TAG_TEMPLATE).replace(r'\%', '%') % '(.+)'), readme)

    for section_name in sections:
        move_tag = MOVE_TAG_TEMPLATE % section_name

        sections = re.findall(rf'(?sm)(^# {re.escape(section_name)}.+?)(?=^# )', readme)
        if len(sections) < 1:
            raise Exception(f'The section {section_name} does not exist')
            readme = readme.replace(sections[0], '', 1).replace(move_tag, sections[0], 1)
    return readme