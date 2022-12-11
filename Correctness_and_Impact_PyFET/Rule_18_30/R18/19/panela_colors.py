# vim: encoding=utf-8

import os
import sys
import colored
import itertools
from globals import MYDIR

"""

After panela will be ready for it, it will be split out in a separate project,
that will be used for all chubin's console services.
There are several features that not yet implemented (see ___doc___ in Panela)

TODO:
    * html output
    * png output

"""

from wcwidth import wcswidth
from colors import find_nearest_color, HEX_TO_ANSI, rgb_from_str
import pyte

# http://stackoverflow.com/questions/19782975/convert-rgb-color-to-the-nearest-color-in-palette-web-safe-color

try:
    basestring        # Python 2
except NameError:
    basestring = str  # Python 3
