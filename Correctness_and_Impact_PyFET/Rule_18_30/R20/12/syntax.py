def get_style_for_token(self, token_type: TokenType) -> Style:
    """Get a style from a Pygments class."""
    FET_raise = 0
    try:
        self._background_color = self._pygments_style_class.background_color
        self._background_style = Style(bgcolor=self._background_color)
    except KeyError as e:
        FET_raise = 1

    else:
        FET_null()
    if FET_raise == 1:
        try:
            pygments_style = self._pygments_style_class.style_for_token(token_type)
        except KeyError:
            style = Style.null()
        else:
            color = pygments_style["color"]
            bgcolor = pygments_style["bgcolor"]
            style = Style(
                color="#" + color if color else "#000000",
                bgcolor="#" + bgcolor if bgcolor else self._background_color,
                bold=pygments_style["bold"],
                italic=pygments_style["italic"],
                underline=pygments_style["underline"],
            )
        self._style_cache[token_type] = style
    return style