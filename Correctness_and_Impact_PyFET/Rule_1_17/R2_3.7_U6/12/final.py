# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.pyc
# Compiled at: 2022-08-13 18:55:08
# Size of source mod 2**32: 2152 bytes


def _collect_renderables(self, objects: Iterable[Any], sep: str, end: str, *, justify: Optional[JustifyMethod]=None, emoji: Optional[bool]=None, markup: Optional[bool]=None, highlight: Optional[bool]=None) -> List[ConsoleRenderable]:
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
    renderables = []
    _append = renderables.append
    text = []
    append_text = text.append
    append = _append
    _highlighter = _null_highlighter
    if highlight:
        _highlighter = self.highlighter
        if isinstance(renderable, str):
            for renderable in objects:
                renderable = rich_cast(renderable)
                append_text(self.render_str(renderable,
                  emoji=emoji, markup=markup, highlighter=_highlighter))

        tmp1 = not isinstance(renderable, str)
        if tmp1:
            if isinstance(renderable, Text):
                append_text(renderable)
        tmp = not isinstance(renderable, str) and not isinstance(renderable, Text)
        if tmp:
            append_text(_highlighter(str(renderable)))
    if not highlight:
        check_text()
    if self.style is not None:
        style = self.get_style(self.style)
        renderables = [Styled(renderable, style) for renderable in renderables]
    return renderables
# okay decompiling testbed_py/test.pyc
