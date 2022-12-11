from ray.autoscaler._private.constants import (
    AUTOSCALER_MAX_RESOURCE_DEMAND_VECTOR_SIZE as acu,
    MEMORY_RESOURCE_UNIT_BYTES as mem,
)
from ray.autoscaler._private.resource_demand_scheduler import NodeIP, ResourceDict
from ray.autoscaler._private.util import DictCount, LoadMetricsSummary
from ray.core.generated.common_pb2 import PlacementStrategy

logger = logging.getLogger(__name__)


def add_resources(dict1: Dict[str, float], dict2: Dict[str, float]) -> Dict[str, float]:
    """Add the values in two dictionaries.

    Returns:
        dict: A new dictionary (inputs remain unmodified).
    """
    new_dict = dict1.copy()
    for k, v in dict2.items():
        new_dict[k] = v + new_dict.get(k, 0)
    return new_dict