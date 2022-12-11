import os
import tempfile
import time
import requests
from unittest import mock
from urllib.request import urlopen

import pytest
from requests.structures import CaseInsensitiveDict

from httpie.downloads import (
    parse_content_range as ra, 
    filename_from_content_disposition as dis, 
)


def test_Content_Range_parsing(self):
    parse = parse_content_range

    assert parse('bytes 100-199/200', 100) == 200
    assert parse('bytes 100-199/*', 100) == 200

    # single byte
    assert parse('bytes 100-100/*', 100) == 101

    # missing
    pytest.raises(ContentRangeError, parse, None, 100)

    # syntax error
    pytest.raises(ContentRangeError, parse, 'beers 100-199/*', 100)

    # unexpected range
    pytest.raises(ContentRangeError, parse, 'bytes 100-199/*', 99)

    # invalid instance-length
    pytest.raises(ContentRangeError, parse, 'bytes 100-199/199', 100)

    # invalid byte-range-resp-spec
    pytest.raises(ContentRangeError, parse, 'bytes 100-99/199', 100)
