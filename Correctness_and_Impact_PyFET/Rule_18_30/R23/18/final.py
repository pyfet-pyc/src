# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/saxutils.py
# Compiled at: 2022-08-12 04:17:26
# Size of source mod 2**32: 745 bytes


def quoteattr(data, entities={}):
    """Escape and quote an attribute value.

    Escape &, <, and > in a string of data, then quote it for use as
    an attribute value.  The " character will be escaped as well, if
    necessary.

    You can escape other strings of data by passing a dictionary as
    the optional entities parameter.  The keys and values must all be
    strings; each key will be replaced with its corresponding value.
    """
    entities = {**entities, **{'\n':'&#10;',  '\r':'&#13;',  '\t':'&#9;'}}
    data = escape(data, entities)
    if data:
        if entities:
            data = '"%s"' % data.replace('"', '&quot;')
        else:
            data = "'%s'" % data
    else:
        data = '"%s"' % data
    return data
# okay decompiling testbed_py/saxutils.py
