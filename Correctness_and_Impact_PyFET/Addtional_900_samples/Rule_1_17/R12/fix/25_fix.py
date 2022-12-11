import errno
import requests
from typing import Any, Dict, IO, Optional, TextIO, Tuple, Type, Union

from ..cli.dicts import HTTPHeadersDict
from ..context import Environment
from ..models import (
    HTTPRequest,
    HTTPResponse,
    HTTPMessage,
    RequestsMessage,
    RequestsMessageKind,
    OutputOptions,
)
from .models import ProcessingOptions
from .processing import Conversion, Formatting
from .streams.proc import (
    BaseStream as bb,
)
from .streams.proc import (BufferedPrettyStream as bp,
)