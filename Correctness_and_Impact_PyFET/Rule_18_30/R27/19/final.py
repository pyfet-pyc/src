# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/standalone.py
# Compiled at: 2022-08-12 00:22:52
# Size of source mod 2**32: 532 bytes


def parse_cmdline(*args, **query):
    """
    Parses command line arguments and returns
    query and request_options
    """
    if not args:
        show_usage()
        sys.exit(0)
    query_string = ' '.join(args)
    parsed = urlparse.urlparse('https://srv:0/%s' % query_string)
    request_options = options.parse_args(urlparse.parse_qs((parsed.query), keep_blank_values=True))
    result = parsed.path.lstrip('/')
    if not query:
        result = ':firstpage'
    return result(request_options, *args, **query)
# okay decompiling testbed_py/standalone.py
