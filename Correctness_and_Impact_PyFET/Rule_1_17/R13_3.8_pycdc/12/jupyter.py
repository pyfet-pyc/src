import builtins
import collections
import dataclasses
import inspect
import os
import sys
from array import array
from collections import Counter, UserDict, UserList, defaultdict, deque
from dataclasses import dataclass, fields, is_dataclass
from inspect import isclass
from itertools import islice
from types import MappingProxyType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    DefaultDict,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

from rich.repr import RichReprResult

try:
    import attr as _attr_module

    _has_attrs = True
except ImportError:  # pragma: no cover
    _has_attrs = False

from . import get_console
from ._loop import loop_last
from ._pick import pick_bool
from .abc import RichRenderable
from .cells import cell_len
from .highlighter import ReprHighlighter
from .jupyter import JupyterMixin, JupyterRenderable
from .measure import Measurement
from .text import Text

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        HighlighterType,
        JustifyMethod,
        OverflowMethod,
        RenderResult,
    )


JUPYTER_CLASSES_TO_NOT_RENDER = {
    # Matplotlib "Artists" manage their own rendering in a Jupyter notebook, and we should not try to render them too.
    # "Typically, all [Matplotlib] visible elements in a figure are subclasses of Artist."
    "matplotlib.artist.Artist",
}