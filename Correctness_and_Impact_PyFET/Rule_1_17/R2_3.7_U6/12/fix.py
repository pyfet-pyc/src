def _collect_renderables(
    self,
    objects: Iterable[Any],
    sep: str,
    end: str,
    *,
    justify: Optional[JustifyMethod] = None,
    emoji: Optional[bool] = None,
    markup: Optional[bool] = None,
    highlight: Optional[bool] = None,
) -> List[ConsoleRenderable]:
    """Combine a number of renderables and text into one renderable.

    Args:
        objects (Iterable[Any]): Anything that Rich can render.
        sep (str): String to write between print data.
        end (str): String to write at end of print data.
        justify (str, optional): One of "left", "right", "center", or "full". Defaults to ``None``.
        emoji (Optional[bool], optional): Enable emoji code, or ``None`` to use console default.
        markup (Optional[bool], optional): Enable markup, or ``None`` to use console default.
        highlight (Optional[bool], optional): Enable automatic highlighting, or ``None`` to use console default.

    Returns:
        List[ConsoleRenderable]: A list of things to render.
    """
    renderables: List[ConsoleRenderable] = []
    _append = renderables.append
    text: List[Text] = []
    append_text = text.append

    append = _append

    _highlighter: HighlighterType = _null_highlighter
    if highlight:
        _highlighter = self.highlighter
        if isinstance(renderable, str):
            for renderable in objects:
                renderable = rich_cast(renderable)
                append_text(
                    self.render_str(
                        renderable, emoji=emoji, markup=markup, highlighter=_highlighter
                    )
            )
        tmp1 = not isinstance(renderable, str)
        if tmp1 and isinstance(renderable, Text):
            append_text(renderable)

        tmp = not isinstance(renderable, str) and not isinstance(renderable, Text)
        if tmp:
        # else:
            append_text(_highlighter(str(renderable)))
    if not highlight:
    # else:
        check_text()

    if self.style is not None:
        style = self.get_style(self.style)
        renderables = [Styled(renderable, style) for renderable in renderables]

    return renderables