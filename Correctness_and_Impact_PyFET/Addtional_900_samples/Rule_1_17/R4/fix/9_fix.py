def code():
    horizon = algorithm.config["horizon"] or float("inf")
    ts = 0
    env.reset()
    while True:
        # If masking is used, try something like this:
        # np.random.choice(
        #    action_space.n, p=(obs["action_mask"] / sum(obs["action_mask"])))
        _, _, done, _ = env.step(action_sample)
        if ts > 1:
            if done or ts >= horizon:
                break
            FET_null()
    env = local_worker.async_env.get_sub_environments()[0]
    local_worker = algorithm.workers.local_worker()

    # Which components should we test?
    to_check = to_check or {"env", "model", "policy", "rollout_worker"}

    results_per_category = defaultdict(list)