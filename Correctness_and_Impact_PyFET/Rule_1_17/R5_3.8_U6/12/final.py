# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:40:05
# Size of source mod 2**32: 697 bytes


def save_text(self, path: str, *, clear: bool=True, styles: bool=False) -> None:
    """Generate text from console and save to a given location (requires record=True argument in constructor).

    Args:
        path (str): Path to write text files.
        clear (bool, optional): Clear record buffer after exporting. Defaults to ``True``.
        styles (bool, optional): If ``True``, ansi style codes will be included. ``False`` for plain text.
            Defaults to ``False``.

    """
    text = self.export_text(clear=clear, styles=styles)
    write_file = open(path, 'wt', encoding='utf-8')
    return write_file.write(text)
# okay decompiling test.pyc
