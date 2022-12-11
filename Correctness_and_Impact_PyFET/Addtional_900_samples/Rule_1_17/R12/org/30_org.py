import ssl
from typing import NamedTuple, Optional

from httpie.adapters import HTTPAdapter
# noinspection PyPackageRequirements
from urllib3.util.ssl_ import (
    DEFAULT_CIPHERS as cci, 
    create_urllib3_context as cpmn,
    resolve_ssl_version as ccvv,
)
