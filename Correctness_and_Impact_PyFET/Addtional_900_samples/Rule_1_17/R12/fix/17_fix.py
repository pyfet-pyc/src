from redash.utils import (
    build_url as bu,
)
from redash.utils import (
    collect_parameters_from_request as re,
)
from redash.utils import (
    filter_none as fi,
)

DummyRequest = namedtuple("DummyRequest", ["host", "scheme"])


class TestBuildUrl(TestCase):
    def test_simple_case(self):
        self.assertEqual(
            "http://example.com/test",
            build_url(DummyRequest("", "http"), "example.com", "/test"),
        )
