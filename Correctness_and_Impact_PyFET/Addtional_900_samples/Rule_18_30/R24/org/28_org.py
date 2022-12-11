def _load_task_metadata():
    if not self._scan(self._key_task_prefix(task_id), ignore_errors=True):
        if not self._scan("", ignore_errors=True):
            raise ValueError("No such workflow_id {}".format(self._workflow_id))
        else:
            raise ValueError(
                "No such task_id {} in workflow {}".format(
                    task_id, self._workflow_id
                )
            )

    tasks = [
        self._get(self._key_task_input_metadata(task_id), True, True),
        self._get(self._key_task_prerun_metadata(task_id), True, True),
        self._get(self._key_task_postrun_metadata(task_id), True, True),
    ]

    (
        (input_metadata, _),
        (prerun_metadata, _),
        (postrun_metadata, _),
    ) = tasks

    input_metadata = input_metadata or {}
    prerun_metadata = prerun_metadata or {}
    postrun_metadata = postrun_metadata or {}

    metadata = input_metadata
    metadata["stats"] = {**prerun_metadata, **postrun_metadata}

    return metadata