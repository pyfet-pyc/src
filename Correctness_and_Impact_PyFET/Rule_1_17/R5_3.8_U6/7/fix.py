def read_file(path):
    FET_raise = 0
    try:
        # with open(path, 'r') as f:
        f = open(path, 'r')
        return f.read()
    except Exception as ex:  # pylint: disable=broad-except
        FET_raise = 1
    
    if FET_raise == 1:
        print('%s:%d:%d: unable to read required file %s' % (path, 0, 0, re.sub(r'\s+', ' ', str(ex))))