def update_frame(self, frame):
    """Updates the frame viewer to use a new frame."""
    self.frame = frame
    lineno = self.frame.lineno or None
    filename = self.frame.filename.strip()
    if inspect.getmodulename(filename):
      if filename not in self._file_cache:
        try:
          with open(filename, "r") as fp:
            self._file_cache[filename] = fp.read()
          source = self._file_cache[filename]
          highlight = lineno
          linenostart = 1
        except FileNotFoundError:
          source = "\n".join(frame.source)
          highlight = min(frame.offset + 1, len(frame.source) - 1)
          linenostart = lineno - frame.offset
    else:
      source = "\n".join(frame.source)
      highlight = min(frame.offset + 1, len(frame.source) - 1)
      linenostart = lineno - frame.offset
    self._header.clear()
    self._header.update(
        colab_lib.div(
            colab_lib.pre(colab_lib.code(f"{html.escape(filename)}({lineno})")),
            style=colab_lib.style({
                "padding": "5px 5px 5px 5px",
                "background-color": "var(--colab-highlighted-surface-color)",
            })))
    self._code_view.update_code(source, [highlight], linenostart=linenostart)
