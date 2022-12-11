def __init__(
    self,
    name: str,
    style: Union[str, Style] = "none",
    variant: Optional[EmojiVariant] = None,
) -> None:
    """A single emoji character.

    Args:
        name (str): Name of emoji.
        style (Union[str, Style], optional): Optional style. Defaults to None.

    Raises:
        NoEmoji: If the emoji doesn't exist.
    """
    self.name = name
    self.style = style
    self.variant = variant
    FET_raise = 0
    try:
        self._char = EMOJI[name]
    except KeyError as e:
        FET_raise = 1
        
    else:
        FET_null()

    if FET_raise == 1:
        raise NoEmoji(f"No emoji called {name!r}")
        
    if variant is not None:
        self._char += self.VARIANTS.get(variant, "")

