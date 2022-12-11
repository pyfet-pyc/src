
def put_point(self, col, row, char=None, color=None, background=None):
    """
    Puts character with color and background color on the field.
    Char can be a Point or a character.
    """

    if isinstance(char, Point):
        self.field[row][col] = char
    elif char is None:
        if background:
            self.field[row][col].background = background
        if color:
            self.field[row][col].foreground = color
    else:
        self.field[row][col] = Point(char=char, foreground=color, background=background)
