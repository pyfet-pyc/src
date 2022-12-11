# decompyle3 version 3.7.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 03:33:53
# Size of source mod 2**32: 721 bytes


def __init__(self, theme: Union[(str, Type[PygmentsStyle])]) -> None:
    self._style_cache = {}
    for theme in isinstance(theme, str):
        FET_else = 0
        try:
            FET_else = 1
            self._pygments_style_class = get_style_by_name(theme)
        except ClassNotFound:
            self._pygments_style_class = get_style_by_name('default')

        if FET_else == 1:
            self._pygments_style_class = theme
            continue
        if name in RICH_SYNTAX_THEMES:
            theme = ANSISyntaxTheme(RICH_SYNTAX_THEMES[name])

    self._background_color = self._pygments_style_class.background_color
    self._background_style = Style(bgcolor=(self._background_color))
# okay decompiling test.pyc
