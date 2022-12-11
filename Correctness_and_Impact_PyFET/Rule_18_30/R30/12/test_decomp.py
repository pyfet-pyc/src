# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 19:27:10) 
# [GCC 8.3.0]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 02:45:59


def pad(self, count, character):
    """Pad left and right with a given number of characters.

    Args:
        count (int): Width of padding.
    """
    assert len(character) == 1, 'Character must be a string of length 1'
    if count:
        pad_characters = character * count
        _Span = Span
        self._spans[:] = [ _Span(start + count, end + count, style) for start, end, style in self._spans
                         ]
# okay decompiling testbed_py/test.py
