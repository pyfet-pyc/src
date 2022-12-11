# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/style.py
# Compiled at: 2022-08-12 03:41:39
# Size of source mod 2**32: 865 bytes


def _add(self, style: Optional['Style']) -> 'Style':
    if self._null:
        return style
    new_style = self.__new__(Style)
    new_style._ansi = None
    new_style._style_definition = None
    new_style._color = style._color or self._color
    new_style._bgcolor = style._bgcolor or self._bgcolor
    new_style._attributes = self._attributes & ~style._set_attributes | style._attributes & style._set_attributes
    new_style._set_attributes = self._set_attributes | style._set_attributes
    new_style._link = style._link or self._link
    new_style._link_id = style._link_id or self._link_id
    new_style._null = style._null
    if self._meta and style._meta:
        new_style._meta = dumps({**(self.meta), **(style.meta)})
    else:
        new_style._meta = self._meta or style._meta
    new_style._hash = None
    return new_style
# okay decompiling testbed_py/style.py
