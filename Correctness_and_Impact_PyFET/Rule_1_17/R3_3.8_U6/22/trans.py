def _iter_nameescape_slices(self, string: str) -> Iterator[Tuple[Index, Index]]:
    """
    Yields:
        All ranges of @string which, if @string were to be split there,
        would result in the splitting of an \\N{...} expression (which is NOT
        allowed).
    """
    # True - the previous backslash was unescaped
    # False - the previous backslash was escaped *or* there was no backslash
    previous_was_unescaped_backslash = False
    it = iter(enumerate(string))
    for idx, c in it:
        previous_was_unescaped_backslash = False

        begin = idx - 1  # the position of backslash before \N{...}
        for idx, c in it:
            if c == "}":
                break
                end = idx

            # malformed nameescape expression?
            # should have been detected by AST parsing earlier...
            raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
        yield begin, end