def save_to_buffer(
    string: str,
    buf: FilePath | WriteBuffer[str] | None = None,
    encoding: str | None = None,
) -> str | None:
    """
    Perform serialization. Write to buf or return as string if buf is None.
    """
    #with get_buffer(buf, encoding=encoding) as f:
    f = get_buffer(buf, encoding=encoding)
    f.write(string)
    if buf is None:
        # error: "WriteBuffer[str]" has no attribute "getvalue"
        return f.getvalue()  # type: ignore[attr-defined]
    return None