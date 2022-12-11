# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:23:49
# Size of source mod 2**32: 1034 bytes


def get_style_for_token(self, token_type: TokenType) -> Style:
    """Get a style from a Pygments class."""
    FET_raise = 0
    try:
        self._background_color = self._pygments_style_class.background_color
        self._background_style = Style(bgcolor=(self._background_color))
    except KeyError as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        try:
            pygments_style = self._pygments_style_class.style_for_token(token_type)
        except KeyError:
            style = Style.null()
        else:
            color = pygments_style['color']
            bgcolor = pygments_style['bgcolor']
            style = Style(color=('#' + color if color else '#000000'),
              bgcolor=('#' + bgcolor if bgcolor else self._background_color),
              bold=(pygments_style['bold']),
              italic=(pygments_style['italic']),
              underline=(pygments_style['underline']))
        self._style_cache[token_type] = style
    return style
# okay decompiling testbed_py/test.py
