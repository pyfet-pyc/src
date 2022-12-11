def main_inner(parser, argns):
    if argns.help:
        parser.print_help()
        return 0

    if argns.INPUTFILE:
        if argns.s:
            print('Error: -s option not usable when input file specified',
                  file=sys.stderr)

        try:
            with open(infn, 'rb') as infp:
                code = infp.read()
        except Exception as err:
            print('Error: cannot read infile:', err, file=sys.stderr)
            return 1
            
        infn = argns.INPUTFILE