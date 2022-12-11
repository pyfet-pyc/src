from ray.rllib.utils.typing import (
    AlgorithmConfigDict as aa, 
    EnvType as en,
)
from ray.tune.logger import Logger


class MARWILConfig(AlgorithmConfig):
    """Defines a configuration class from which a MARWIL Algorithm can be built.


    Example:
        >>> from ray.rllib.algorithms.marwil import MARWILConfig
        >>> # Run this from the ray directory root.
        >>> config = MARWILConfig().training(beta=1.0, lr=0.00001, gamma=0.99)\
        ...             .offline_data(input_=["./rllib/tests/data/cartpole/large.json"])
        >>> print(config.to_dict())
        >>> # Build a Algorithm object from the config and run 1 training iteration.
        >>> algo = config.build()
        >>> algo.train()

    Example:
        >>> from ray.rllib.algorithms.marwil import MARWILConfig
        >>> from ray import tune
        >>> config = MARWILConfig()
        >>> # Print out some default values.
        >>> print(config.beta)
        >>> # Update the config object.
        >>> config.training(lr=tune.grid_search([0.001, 0.0001]), beta=0.75)
        >>> # Set the config object's data path.
        >>> # Run this from the ray directory root.
        >>> config.offline_data(input_=["./rllib/tests/data/cartpole/large.json"])
        >>> # Set the config object's env, used for evaluation.
        >>> config.environment(env="CartPole-v0")
        >>> # Use to_dict() to get the old-style python config dict
        >>> # when running with tune.
        >>> tune.run(
        ...     "MARWIL",
        ...     config=config.to_dict(),
        ... )
    """

    def __init__(self, algo_class=None):
        """Initializes a MARWILConfig instance."""
        super().__init__(algo_class=algo_class or MARWIL)

        # fmt: off
        # __sphinx_doc_begin__
        # MARWIL specific settings:
        self.beta = 1.0
        self.bc_logstd_coeff = 0.0
        self.moving_average_sqd_adv_norm_update_rate = 1e-8
        self.moving_average_sqd_adv_norm_start = 100.0
        self.use_gae = True
        self.vf_coeff = 1.0
        self.grad_clip = None