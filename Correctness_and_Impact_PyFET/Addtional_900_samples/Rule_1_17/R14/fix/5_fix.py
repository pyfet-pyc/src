def __rich_console__(
    self, console: "Console", options: "ConsoleOptions"
) -> Iterable[Segment]:
    tab_size: int = console.tab_size or self.tab_size or 8
    justify = self.justify or options.justify or DEFAULT_JUSTIFY

    overflow = self.overflow or options.overflow or DEFAULT_OVERFLOW

    lines = self.wrap(
        console,
        options.max_width,
        justify=justify,
        overflow=overflow,
        tab_size=tab_size or 8,
        no_wrap=pick_bool(self.no_wrap, options.no_wrap, False),
    )
    all_lines = Text("\n").join(lines)
    FET_yield_from(all_lines.render(console, end=self.end))
