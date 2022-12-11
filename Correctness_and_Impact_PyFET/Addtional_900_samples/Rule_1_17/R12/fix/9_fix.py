
from ray.tune.search import (
    UNRESOLVED_SEARCH_SPACE as un,
)
from ray.tune.search import (
    UNDEFINED_METRIC_MODE as unnd,
)
from ray.tune.search.variant_generator import parse_spec_vars
from ray.tune.utils.util import flatten_dict, unflatten_list_dict

try:
    import ConfigSpace
    from hpbandster.optimizers.config_generators.bohb import BOHB
except ImportError:
    BOHB = ConfigSpace = None

logger = logging.getLogger(__name__)


class _BOHBJobWrapper:
    """Mock object for HpBandSter to process."""

    def __init__(self, loss: float, budget: float, config: Dict):
        self.result = {"loss": loss}
        self.kwargs = {"budget": budget, "config": config.copy()}
        self.exception = None