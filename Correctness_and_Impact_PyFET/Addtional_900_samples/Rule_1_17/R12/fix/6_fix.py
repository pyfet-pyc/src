from ray.rllib.utils.typing import (
    AlgorithmConfigDict as alg,
)
from ray.rllib.utils.typing import (
    LocalOptimizer as loc,
)
from ray.util.debug import log_once

tf1, tf, tfv = try_import_tf()
logger = logging.getLogger(__name__)


@DeveloperAPI
class EagerTFPolicyV2(Policy):
    """A TF-eageer / TF2 based tensorflow policy.

    This class is intended to be used and extended by sub-classing.
    """

    def __init__(
        self,
        observation_space: gym.spaces.Space,
        action_space: gym.spaces.Space,
        config: AlgorithmConfigDict,
        **kwargs,
    ):
        self.framework = config.get("framework", "tf2")
