# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_traceback.py
# Compiled at: 2022-08-11 20:43:11
# Size of source mod 2**32: 493 bytes


def test_capture():
    exc_type, exc_value, traceback = sys.exc_info()
    sys.excepthook(exc_type, exc_value, traceback)
    rendered_exception = console.file.getvalue()
    r, g, b = (123, 234, 123)
    console = Console(force_terminal=True,
      _environ={'COLORTERM': 'truecolor'},
      theme=(Theme({'traceback.title': f"rgb({r},{g},{b})"})))
    try:
        1 / 0
    except Exception:
        tb = Traceback()
        tb.trace.stacks[0].exc_type = 'ZeroDivisionError'
# okay decompiling testbed_py/test_traceback.py
