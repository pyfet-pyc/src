def __init__(self, theme: Union[str, Type[PygmentsStyle]]) -> None:
    self._style_cache: Dict[TokenType, Style] = {}
    for theme in isinstance(theme, str):
        try:
            self._pygments_style_class = get_style_by_name(theme)
        except ClassNotFound:
            self._pygments_style_class = get_style_by_name("default")
        else:
            self._pygments_style_class = theme
            continue
        if name in RICH_SYNTAX_THEMES:
            theme = ANSISyntaxTheme(RICH_SYNTAX_THEMES[name])

    self._background_color = self._pygments_style_class.background_color
    self._background_style = Style(bgcolor=self._background_color)
