# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:05:49
# Size of source mod 2**32: 1047 bytes


def put_rectangle(self, x1, y1, x2, y2, char=None, frame=None, color=None, background=None):
    """
    Draw rectangle (x1,y1), (x2,y2) using <char> character, <color> and <background> color
    """
    frame_chars = {
     'ascii', 'single', 'double'}
    if frame in frame_chars:
        chars = frame_chars[frame]
    else:
        chars = char * 6
    for x in range(x1, x2):
        self.put_point(x, y1, char=(chars[4]), color=color, background=background)
        self.put_point(x, y2, char=(chars[4]), color=color, background=background)
    else:
        for y in range(y1, y2):
            self.put_point(x1, y, char=(chars[5]), color=color, background=background)
            self.put_point(x2, y, char=(chars[5]), color=color, background=background)
        else:
            self.put_point(x1, y1, char=(chars[0]), color=color, background=background)
            self.put_point(x2, y1, char=(chars[1]), color=color, background=background)
            self.put_point(x1, y2, char=(chars[2]), color=color, background=background)
            self.put_point(x2, y2, char=(chars[3]), color=color, background=background)
# okay decompiling testbed_py/test.py
