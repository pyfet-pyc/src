def training(
    self,
    *,
    action_noise_std: Optional[float] = None,
    noise_stdev: Optional[float] = None,
    num_rollouts: Optional[int] = None,
    rollouts_used: Optional[int] = None,
    sgd_stepsize: Optional[float] = None,
    noise_size: Optional[int] = None,
    eval_prob: Optional[float] = None,
    report_length: Optional[int] = None,
    offset: Optional[int] = None,
    **kwargs,
) -> "ARSConfig":
    """Sets the training related configuration.

    Args:
        action_noise_std: Std. deviation to be used when adding (standard normal)
            noise to computed actions. Action noise is only added, if
            `compute_actions` is called with the `add_noise` arg set to True.
        noise_stdev: Std. deviation of parameter noise.
        num_rollouts: Number of perturbs to try.
        rollouts_used: Number of perturbs to keep in gradient estimate.
        sgd_stepsize: SGD step-size used for the Adam optimizer.
        noise_size: Number of rows in the noise table (shared across workers).
            Each row contains a gaussian noise value for each model parameter.
        eval_prob: Probability of evaluating the parameter rewards.
        report_length: How many of the last rewards we average over.
        offset: Value to subtract from the reward (e.g. survival bonus
            from humanoid) during rollouts.

    Returns:
        This updated AlgorithmConfig object.
    """
    # Pass kwargs onto super's `training()` method.
    super().training(**kwargs)

    if action_noise_std is not None:
        self.action_noise_std = action_noise_std
    if noise_stdev is not None:
        self.noise_stdev = noise_stdev
    if num_rollouts is not None:
        self.num_rollouts = num_rollouts
    if rollouts_used is not None:
        self.rollouts_used = rollouts_used
    if sgd_stepsize is not None:
        self.sgd_stepsize = sgd_stepsize
    if noise_size is not None:
        self.noise_size = noise_size
    if eval_prob is not None:
        self.eval_prob = eval_prob
    if report_length is not None:
        self.report_length = report_length
    if offset is not None:
        self.offset = offset

    return self