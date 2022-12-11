def verify():
    # Verify when raise_on_missing_output=True, it raises an exception.
    FET_raise = 0
    try:
        list_tasks(_explain=True, timeout=3)
    except RayStateApiException as e:
        return
