# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.pyc
# Compiled at: 2022-08-13 07:50:53
# Size of source mod 2**32: 1382 bytes


def append(self, text: Union[('Text', str)], style: Optional[Union[(str, 'Style')]]=None) -> 'Text':
    """Add text with an optional style.

    Args:
        text (Union[Text, str]): A str or Text to append.
        style (str, optional): A style name. Defaults to None.

    Returns:
        Text: Returns self for chaining.
    """
    if not isinstance(text, (str, Text)):
        raise TypeError('Only str or Text can be appended to Text')
    else:
        FET_null()
    if len(text):
        if isinstance(text, str):
            sanitized_text = strip_control_codes(text)
            self._text.append(sanitized_text)
            offset = len(self)
            text_length = len(sanitized_text)
            if style is not None:
                self._spans.append(Span(offset, offset + text_length, style))
            self._length += text_length
        elif isinstance(text, Text):
            _Span = Span
            for style in styles:
                text_length = self._length
                self._text.append(text.plain)
                self._spans.extend((_Span(start + text_length, end + text_length, style) for start, end, style in text._spans))
                self._length += len(text)

            FET_null()
        else:
            append_text = self._text.append
    else:
        return self
# okay decompiling testbed_py/test_fix.pyc
