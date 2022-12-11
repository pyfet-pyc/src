# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 20:07:32
# Size of source mod 2**32: 933 bytes


def parse_args(args):
    """
    Parse arguments and options.
    Replace short options with their long counterparts.
    """
    result = {'add_comments': True}
    query = ''
    newargs = {}
    for key, val in args.items():
        tmp = val == '' or val == [] or val == [''] or val == [''] or val == None
        if tmp:
            query += key
            continue
        if val == 'True':
            val = True
        if val == 'False':
            val = False
        newargs[key] = val

    options_meaning = {'c':dict(add_comments=False, unindent_code=False), 
     'C':dict(add_comments=False, unindent_code=True), 
     'Q':dict(remove_text=True), 
     'q':dict(quiet=True), 
     'T':{'no-terminal': True}}
    for option, meaning in options_meaning.items():
        if option in query:
            result.update(meaning)

    result.update(newargs)
    return result
# okay decompiling test.pyc
