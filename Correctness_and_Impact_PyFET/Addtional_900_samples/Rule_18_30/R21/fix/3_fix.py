def main_inner(parser, argns):
    if argns.help:
        parser.print_help()
        return 0

    if argns.V:
        print('Pygments version %s, (c) 2006-2022 by Georg Brandl, Matthäus '
              'Chajdas and contributors.' % __version__)
        return 0

    def is_only_option(opt):
        return not any(v for (k, v) in vars(argns).items() if k != opt)

    # handle ``pygmentize -L``
    if argns.L is not None:
        arg_set = set()
        for k, v in vars(argns).items():
            if v:
                arg_set.add(k)

        arg_set.discard('L')
        arg_set.discard('json')

        if arg_set:
            parser.print_help(sys.stderr)
            return 2

        # print version
        if not argns.json:
            main(['', '-V'])
        allowed_types = {'lexer', 'formatter', 'filter', 'style'}
        largs = [arg.rstrip('s') for arg in argns.L]
        if any(arg not in allowed_types for arg in largs):
            parser.print_help(sys.stderr)
            return 0
        if not largs:
            largs = allowed_types
        if not argns.json:
            for arg in largs:
                _print_list(arg)
        else:
            _print_list_as_json(largs)
        return 0

    # handle ``pygmentize -H``
    if argns.H:
        if not is_only_option('H'):
            parser.print_help(sys.stderr)
            return 2
        what, name = argns.H
        if what not in ('lexer', 'formatter', 'filter'):
            parser.print_help(sys.stderr)
            return 2
        return _print_help(what, name)

    # parse -O options
    parsed_opts = _parse_options(argns.O or [])

    # parse -P options
    for p_opt in argns.P or []:
        try:
            name, value = p_opt.split('=', 1)
        except ValueError:
            parsed_opts[p_opt] = True
        else:
            parsed_opts[name] = value

    # encodings
    inencoding = parsed_opts.get('inencoding', parsed_opts.get('encoding'))
    outencoding = parsed_opts.get('outencoding', parsed_opts.get('encoding'))

    # handle ``pygmentize -N``
    if argns.N:
        lexer = find_lexer_class_for_filename(argns.N)
        if lexer is None:
            lexer = TextLexer

        print(lexer.aliases[0])
        return 0

    # handle ``pygmentize -C``
    if argns.C:
        inp = sys.stdin.buffer.read()
        try:
            lexer = guess_lexer(inp, inencoding=inencoding)
        except ClassNotFound:
            lexer = TextLexer

        print(lexer.aliases[0])
        return 0

    # handle ``pygmentize -S``
    S_opt = argns.S
    a_opt = argns.a
    if S_opt is not None:
        f_opt = argns.f
        if not f_opt:
            parser.print_help(sys.stderr)
            return 2
        if argns.l or argns.INPUTFILE:
            parser.print_help(sys.stderr)
            return 2

        try:
            parsed_opts['style'] = S_opt
            fmter = get_formatter_by_name(f_opt, **parsed_opts)
        except ClassNotFound as err:
            print(err, file=sys.stderr)
            return 1

        print(fmter.get_style_defs(a_opt or ''))
        return 0

    # if no -S is given, -a is not allowed
    if argns.a is not None:
        parser.print_help(sys.stderr)
        return 2

    # parse -F options
    F_opts = _parse_filters(argns.F or [])

    # -x: allow custom (eXternal) lexers and formatters
    allow_custom_lexer_formatter = bool(argns.x)

    # select lexer
    lexer = None

    # given by name?
    lexername = argns.l
    if lexername:
        # custom lexer, located relative to user's cwd
        if allow_custom_lexer_formatter and '.py' in lexername:
            try:
                filename = None
                name = None
                if ':' in lexername:
                    filename, name = lexername.rsplit(':', 1)

                    if '.py' in name:
                        # This can happen on Windows: If the lexername is
                        # C:\lexer.py -- return to normal load path in that case
                        name = None

                if filename and name:
                    lexer = load_lexer_from_file(filename, name,
                                                 **parsed_opts)
                else:
                    lexer = load_lexer_from_file(lexername, **parsed_opts)
            except ClassNotFound as err:
                print('Error:', err, file=sys.stderr)
                return 1
        else:
            try:
                lexer = get_lexer_by_name(lexername, **parsed_opts)
            except (OptionError, ClassNotFound) as err:
                print('Error:', err, file=sys.stderr)
                return 1

    # read input code
    code = None

    if argns.INPUTFILE:
        if argns.s:
            print('Error: -s option not usable when input file specified',
                  file=sys.stderr)
            return 2

        infn = argns.INPUTFILE
        try:
            with open(infn, 'rb') as infp:
                code = infp.read()
        except Exception as err:
            print('Error: cannot read infile:', err, file=sys.stderr)
            return 1
        if not inencoding:
            code, inencoding = guess_decode(code)

        # do we have to guess the lexer?
        if not lexer:
            try:
                lexer = get_lexer_for_filename(infn, code, **parsed_opts)
            except ClassNotFound as errs:
                if argns.g:
                    try:
                        lexer = guess_lexer(code, **parsed_opts)
                    except ClassNotFound as e:
                        lexer = TextLexer(**parsed_opts)
                else:
                    print('Error:', err, file=sys.stderr)
                    return 1
            except OptionError as errs:
                print('Error:', err, file=sys.stderr)
                return 1
