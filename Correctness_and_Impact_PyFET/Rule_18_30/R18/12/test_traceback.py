def test_capture():
    exc_type, exc_value, traceback = sys.exc_info()
    sys.excepthook(exc_type, exc_value, traceback)
    rendered_exception = console.file.getvalue()
    r, g, b = 123, 234, 123
    console = Console(
        force_terminal=True,
        _environ={"COLORTERM": "truecolor"},
        theme=Theme({"traceback.title": f"rgb({r},{g},{b})"}),
    )
    try:
        1 / 0
    except Exception:
        tb = Traceback()
        tb.trace.stacks[0].exc_type = "ZeroDivisionError"