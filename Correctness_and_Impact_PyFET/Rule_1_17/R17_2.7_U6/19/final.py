# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/panela_colors.py
# Compiled at: 2022-08-11 19:49:03
# Size of source mod 2**32: 534 bytes


def put_point(self, col, row, char=None, color=None, background=None):
    """
    Puts character with color and background color on the field.
    Char can be a Point or a character.
    """
    if isinstance(char, Point):
        self.field[row][col] = char
    else:
        if char is None:
            if background:
                self.field[row][col].background = background
            if color:
                self.field[row][col].foreground = color
        else:
            self.field[row][col] = Point(char=char, foreground=color, background=background)
# okay decompiling testbed_py/panela_colors.py
