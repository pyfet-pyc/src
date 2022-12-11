# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 17:11:05
# Size of source mod 2**32: 497 bytes


def _repr_mimebundle_(self: 'ConsoleRenderable', include: Sequence[str], exclude: Sequence[str], **kwargs: Any) -> Dict[(str, str)]:
    console = get_console()
    segments = list(console.render(self, console.options))
    html = _render_segments(segments)
    text = console._render_buffer(segments)
    data = {'text/plain':text,  'text/html':html}
    if include:
        data = foo()
    return data


def foo():
    return {v:k for k, v in data.items() if k in include if k in include}
# okay decompiling test.pyc
