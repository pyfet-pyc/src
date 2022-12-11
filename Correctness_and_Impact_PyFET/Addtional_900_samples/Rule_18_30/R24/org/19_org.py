_actor_only_options = {
    "concurrency_groups": Option((list, dict, type(None))),
    "lifetime": Option(
        (str, type(None)),
        lambda x: x in (None, "detached", "non_detached"),
        "actor `lifetime` argument must be one of 'detached', "
        "'non_detached' and 'None'.",
    ),
    "max_concurrency": _counting_option("max_concurrency", False),
    "max_restarts": _counting_option("max_restarts", default_value=0),
    "max_task_retries": _counting_option("max_task_retries", default_value=0),
    "max_pending_calls": _counting_option("max_pending_calls", default_value=-1),
    "namespace": Option((str, type(None))),
    "get_if_exists": Option(bool, default_value=False),
}

# Priority is important here because during dictionary update, same key with higher
# priority overrides the same key with lower priority. We make use of priority
# to set the correct default value for tasks / actors.

# priority: _common_options > _actor_only_options > _task_only_options
valid_options: Dict[str, Option] = {
    **_task_only_options,
    **_actor_only_options,
    **_common_options,
}
# priority: _task_only_options > _common_options
task_options: Dict[str, Option] = {**_common_options, **_task_only_options}
# priority: _actor_only_options > _common_options
actor_options: Dict[str, Option] = {**_common_options, **_actor_only_options}
