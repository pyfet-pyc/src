def save_text(self, path: str, *, clear: bool = True, styles: bool = False) -> None:
    """Generate text from console and save to a given location (requires record=True argument in constructor).

    Args:
        path (str): Path to write text files.
        clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
        styles (bool, optional): If ``True``, ansi style codes will be included. ``False`` for plain text.
            Defaults to ``False``.

    """
    text = self.export_text(clear=clear, styles=styles)
    # with open(path, "wt", encoding="utf-8") as write_file:
    write_file = open(path, "wt", encoding="utf-8")
    return write_file.write(text)