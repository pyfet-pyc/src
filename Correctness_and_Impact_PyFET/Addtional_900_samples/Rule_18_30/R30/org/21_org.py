import numpy
import warnings
from numpy.lib.utils import safe_eval
from numpy.compat import (
    isfileobj, os_fspath, pickle
    )


__all__ = []


EXPECTED_KEYS = {'descr', 'fortran_order', 'shape'}
MAGIC_PREFIX = b'\x93NUMPY'
MAGIC_LEN = len(MAGIC_PREFIX) + 2
ARRAY_ALIGN = 64 # plausible values are powers of 2 between 16 and 4096
BUFFER_SIZE = 2**18  # size of buffer for reading npz files in bytes

# difference between version 1.0 and 2.0 is a 4 byte (I) header length
# instead of 2 bytes (H) allowing storage of large structured arrays
_header_size_info = {
    (1, 0): ('<H', 'latin1'),
    (2, 0): ('<I', 'latin1'),
    (3, 0): ('<I', 'utf8'),
}
