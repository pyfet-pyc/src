# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/segment.py
# Compiled at: 2022-08-11 19:46:54
# Size of source mod 2**32: 680 bytes


@classmethod
def remove_color(cls, segments: Iterable['Segment']) -> Iterable['Segment']:
    """Remove all color from an iterable of segments.

    Args:
        segments (Iterable[Segment]): An iterable segments.

    Yields:
        Segment: Segments with colorless style.
    """
    cache = {}
    for text, style, control in segments:
        if style:
            colorless_style = cache.get(style)
            if colorless_style is None:
                colorless_style = style.without_color
                cache[style] = colorless_style
            yield cls(text, colorless_style, control)
        else:
            yield cls(text, None, control)
# okay decompiling testbed_py/segment.py
