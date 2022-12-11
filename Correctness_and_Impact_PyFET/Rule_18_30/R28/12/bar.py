from typing import Optional, Union

from .color import Color
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style

# There are left-aligned characters for 1/8 to 7/8, but
# the right-aligned characters exist only for 1/8 and 4/8.
BEGIN_BLOCK_ELEMENTS = ["█", "█", "█", "▐", "▐", "▐", "▕", "▕"]
END_BLOCK_ELEMENTS = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉"]
FULL_BLOCK = "█"

