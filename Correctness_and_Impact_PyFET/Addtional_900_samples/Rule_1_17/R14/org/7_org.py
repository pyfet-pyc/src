def _render_pulse(
    self, console: Console, width: int, ascii: bool = False
) -> Iterable[Segment]:
    """Renders the pulse animation.

    Args:
        console (Console): Console instance.
        width (int): Width in characters of pulse animation.

    Returns:
        RenderResult: [description]

    Yields:
        Iterator[Segment]: Segments to render pulse
    """
    fore_style = console.get_style(self.pulse_style, default="white")
    back_style = console.get_style(self.style, default="black")

    pulse_segments = self._get_pulse_segments(
        fore_style, back_style, console.color_system, console.no_color, ascii=ascii
    )
    segment_count = len(pulse_segments)
    current_time = (
        monotonic() if self.animation_time is None else self.animation_time
    )
    segments = pulse_segments * (int(width / segment_count) + 2)
    offset = int(-current_time * 15) % segment_count
    segments = segments[offset : offset + width]
    yield from segments