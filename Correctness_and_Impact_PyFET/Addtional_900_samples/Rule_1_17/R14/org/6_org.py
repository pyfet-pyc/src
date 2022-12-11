def _get_syntax(
    self,
    console: Console,
    options: ConsoleOptions,
) -> Iterable[Segment]:
    """
    Get the Segments for the Syntax object, excluding any vertical/horizontal padding
    """
    transparent_background = self._get_base_style().transparent_background
    code_width = (
        (
            (options.max_width - self._numbers_column_width - 1)
            if self.line_numbers
            else options.max_width
        )
        if self.code_width is None
        else self.code_width
    )

    ends_on_nl, processed_code = self._process_code(self.code)
    text = self.highlight(processed_code, self.line_range)

    if not self.line_numbers and not self.word_wrap and not self.line_range:
        if not ends_on_nl:
            text.remove_suffix("\n")
        # Simple case of just rendering text
        style = (
            self._get_base_style()
            + self._theme.get_style_for_token(Comment)
            + Style(dim=True)
            + self.background_style
        )
        if self.indent_guides and not options.ascii_only:
            text = text.with_indent_guides(self.tab_size, style=style)
            text.overflow = "crop"
        if style.transparent_background:
            yield from console.render(
                text, options=options.update(width=code_width)
            )