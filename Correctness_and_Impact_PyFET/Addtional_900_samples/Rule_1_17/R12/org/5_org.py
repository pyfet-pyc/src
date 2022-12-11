
from ray.tune.search import (
    UNRESOLVED_SEARCH_SPACE as unps,
    UNDEFINED_METRIC_MODE as mode,
)
from ray.tune.search.variant_generator import assign_value, parse_spec_vars
from ray.tune.utils import flatten_dict

try:
    hyperopt_logger = logging.getLogger("hyperopt")
    hyperopt_logger.setLevel(logging.WARNING)
    import hyperopt as hpo
    from hyperopt.pyll import Apply
except ImportError:
    hpo = None
    Apply = None
