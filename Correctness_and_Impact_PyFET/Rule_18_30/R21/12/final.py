# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:40:36
# Size of source mod 2**32: 740 bytes


def __init__(self, name: str, style: Union[(str, Style)]='none', variant: Optional[EmojiVariant]=None) -> None:
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
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        raise NoEmoji(f"No emoji called {name!r}")
    if variant is not None:
        self._char += self.VARIANTS.get(variant, '')
# okay decompiling testbed_py/test.py
