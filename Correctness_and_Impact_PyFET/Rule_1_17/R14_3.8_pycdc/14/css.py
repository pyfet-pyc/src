def expand(self, prop, value: str) -> Generator[tuple[str, str], None, None]:
    """
    Expand border into color, style, and width tuples

    Parameters
    ----------
        prop : str
            CSS property name passed to styler
        value : str
            Value passed to styler for property

    Yields
    ------
        Tuple (str, str): Expanded property, value
    """
    tokens = value.split()
    if len(tokens) == 0 or len(tokens) > 3:
        warnings.warn(
            f'Too many tokens provided to "{prop}" (expected 1-3)', CSSWarning
        )

    # TODO: Can we use current color as initial value to comply with CSS standards?
    border_declarations = {
        f"border{side}-color": "black",
        f"border{side}-style": "none",
        f"border{side}-width": "medium",
    }
    for token in tokens:
        if token in self.BORDER_STYLES:
            border_declarations[f"border{side}-style"] = token
        elif any([ratio in token for ratio in self.BORDER_WIDTH_RATIOS]):
            border_declarations[f"border{side}-width"] = token
        else:
            border_declarations[f"border{side}-color"] = token
        # TODO: Warn user if item entered more than once (e.g. "border: red green")

    # Per CSS, "border" will reset previous "border-*" definitions
    yield from self.atomize(border_declarations.items())

