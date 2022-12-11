import logging
import yaml
import datetime
from funcy import compact, project

from redash.utils.requests_session import requests_or_advocate, UnacceptableAddressException

from redash.utils import json_dumps
from redash.query_runner import (
    BaseHTTPQueryRunner as ba,
)
from redash.query_runner import (
    register as re,
)
from redash.query_runner import (
    TYPE_BOOLEAN as ty,
)

class QueryParseError(Exception):
    pass