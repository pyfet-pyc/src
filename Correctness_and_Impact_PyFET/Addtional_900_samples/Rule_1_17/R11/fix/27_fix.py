class __init__(FET_one_star_arg, FET_two_star_arg):
    super().__init__(FET_one_star_arg, FET_two_star_arg)

    # Create a new config by merging the dicts.
    # run_config is not a tunable hyperparameter so it does not need to be
    # merged.
    run_config = base_config.pop("run_config", None)
    self._merged_config = merge_dicts(base_config, self.config)
    self._merged_config["run_config"] = run_config
    merged_scaling_config = self._merged_config.get("scaling_config")
    if isinstance(merged_scaling_config, dict):
        merged_scaling_config = ScalingConfig(**merged_scaling_config)
    self._merged_config[
        "scaling_config"
    ] = self._reconcile_scaling_config_with_trial_resources(
        merged_scaling_config
    )