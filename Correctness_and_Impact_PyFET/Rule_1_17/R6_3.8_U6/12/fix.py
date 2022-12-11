def _repr_mimebundle_(
    self: "ConsoleRenderable",
    include: Sequence[str],
    exclude: Sequence[str],
    **kwargs: Any,
) -> Dict[str, str]:
    console = get_console()
    segments = list(console.render(self, console.options))
    html = _render_segments(segments)
    text = console._render_buffer(segments)
    data = {"text/plain": text, "text/html": html}
    if include:
        data = foo()
    return data

def foo():
    return {k: v for (k, v) in data.items() if k in include}

