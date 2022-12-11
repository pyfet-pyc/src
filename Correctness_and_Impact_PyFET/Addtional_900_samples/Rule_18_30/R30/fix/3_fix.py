import pytest
import os
try:
    import coverage
except ImportError:
    pytestmark = pytest.mark.skip("coverage not available")


kv_statement_lines = {4, 5, 6, 8, 9, 12, 15, 17}

