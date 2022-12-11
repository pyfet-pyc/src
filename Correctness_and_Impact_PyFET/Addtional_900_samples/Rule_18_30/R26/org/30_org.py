def _edit_titlepage(pdf_dir):
    smanual = os.path.join(pdf_dir, 'sphinxmanual.cls')
    with open(smanual, 'r') as f:
        lines = f.read().split('\n')

    for i, l in enumerate(lines):
        lines[i] = lines[i].replace('\\@date', '')

    with open(smanual, 'w') as f:
        f.write('\n'.join(lines))