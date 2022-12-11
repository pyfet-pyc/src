def read_file(path):
    FET_raise = 0
    try:
        with open(path, 'r') as f:
            f.read()
    except Exception as ex:  # pylint: disable=broad-except
        FET_raise = 1
    else:
        FET_null()
    if FET_raise == 1:
        print('%s:%d:%d: unable to read required file %s' % (path, 0, 0, re.sub(r'\s+', ' ', str(ex))))
        FET_return = 1
    if FET_return:
        return None