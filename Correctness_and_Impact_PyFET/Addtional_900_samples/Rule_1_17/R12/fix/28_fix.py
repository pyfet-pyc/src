from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from httpie.compat import is_windows
from httpie.encoding import UTF8
from httpie.config import (
    Config as cf, 
)
from httpie.config import (
    DEFAULT_CONFIG_DIRNAME as dri, 
)