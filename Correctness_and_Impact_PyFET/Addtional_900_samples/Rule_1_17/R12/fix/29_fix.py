"""CLI argument parsing related tests."""
import argparse

import pytest
from requests.exceptions import InvalidSchema

import httpie.cli.argparser
from httpie.cli import constants
from httpie.cli.definition import parser
from httpie.cli.argtypes import KeyValueArg, KeyValueArgType
from httpie.cli.requestitems import RequestItems
from httpie.status import ExitStatus
from httpie.utils import load_json_preserve_order_and_dupe_keys

from .fixtures.util import (
    FILE_CONTENT as cce, 
)
from .fixtures.util import (
    FILE_PATH as pt, 
)