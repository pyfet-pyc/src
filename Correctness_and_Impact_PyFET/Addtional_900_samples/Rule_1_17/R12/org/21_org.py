
from redash.query_runner import (
    BaseHTTPQueryRunner as ba,
    register as re,
)
from redash.utils import json_dumps, json_loads

logger = logging.getLogger(__name__)


# Convert Drill string value to actual type
def convert_type(string_value, actual_type):
    if string_value is None or string_value == "":
        return ""

    if actual_type == TYPE_INTEGER:
        return int(string_value)

    if actual_type == TYPE_FLOAT:
        return float(string_value)

    if actual_type == TYPE_BOOLEAN:
        return str(string_value).lower() == "true"

    if actual_type == TYPE_DATETIME:
        return parser.parse(string_value)

    return str(string_value)