def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as ex:  # pylint: disable=broad-except
        print('%s:%d:%d: unable to read required file %s' % (path, 0, 0, re.sub(r'\s+', ' ', str(ex))))