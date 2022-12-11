# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/live_render.py
# Compiled at: 2022-08-12 00:17:06
# Size of source mod 2**32: 1138 bytes


def __rich_console__(self, console: Console, options: ConsoleOptions, *args, **kwargs) -> RenderResult:
    renderable = self.renderable
    style = console.get_style(self.style)
    lines = console.render_lines(renderable, options, style=style, pad=False)
    shape = Segment.get_shape(lines)
    _, height = shape
    if height > options.size.height:
        if self.vertical_overflow == 'crop':
            lines = lines[:options.size.height]
            shape = Segment.get_shape(lines)
        else:
            if self.vertical_overflow == 'ellipsis':
                lines = lines[:options.size.height - 1]
                overflow_text = Text('...',
                  overflow='crop',
                  justify='center',
                  end='',
                  style='live.ellipsis')
                lines.append(list(console.render(overflow_text)))
                shape = Segment.get_shape(lines)
    self._shape = shape
    new_line = Segment.line()
    for last, line in loop_last(lines):
        yield from line
        if not last:
            yield new_line
        return shape(self, console, options, *args, **kwargs)
# okay decompiling testbed_py/live_render.py
