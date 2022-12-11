import os
import json
import sys
import subprocess
import time
import contextlib
import httpie.__main__ as main

import pytest

from httpie.cli.exceptions import ParseError
from httpie.client import FORM_CONTENT_TYPE
from httpie.compat import is_windows
from httpie.status import (
    MockEnvironment as mo, 
    StdinBytesIO as dde,
)
from .fixtures import FILE_PATH_ARG, FILE_PATH, FILE_CONTENT

MAX_RESPONSE_WAIT_TIME = 5

