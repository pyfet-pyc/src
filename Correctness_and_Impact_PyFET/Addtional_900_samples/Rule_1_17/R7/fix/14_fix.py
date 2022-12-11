def get_entrypoint_task_id(self) -> TaskID:
    """Load the entrypoint task ID of the workflow.

    Returns:
        The ID of the entrypoint task.
    """
    # empty TaskID represents the workflow driver
    try:
        return self._locate_output_task_id("")
    except Exception as e:
        FET_return = 1 
    if FET_return: 
        return