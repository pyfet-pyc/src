def _compile_iteration_results(self, *args, **kwargs):
    result = super()._compile_iteration_results(*args, **kwargs)
    replay_stats = ray.get(
        self._replay_actors[0].stats.remote(self.config["optimizer"].get("debug"))
    )
    exploration_infos_list = self.workers.foreach_policy_to_train(
        lambda p, pid: {pid: p.get_exploration_state()}
    )
    exploration_infos = {}
    for info in exploration_infos_list:
        # we're guaranteed that each info has policy ids that are unique
        exploration_infos.update(info)
    other_results = {
        "exploration_infos": exploration_infos,
        "learner_queue": self.learner_thread.learner_queue_size.stats(),
        "replay_shard_0": replay_stats,
    }

    result["info"].update(other_results)
    return result