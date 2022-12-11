
def run_command(cmd):
    print('Running %r:' % (cmd))
    os.system(cmd)
    print('------')
    if has_newnumpy:
        try:
            print('Found new numpy version %r in %s' %
                  (numpy.__version__, numpy.__file__))
        except Exception as msg:
            print('error:', msg)
            print('------')
            FET_return = 1 
        if FET_return: 
            return