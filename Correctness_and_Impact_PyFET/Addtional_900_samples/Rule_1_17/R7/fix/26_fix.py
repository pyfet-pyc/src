def verify():
    # Verify when raise_on_missing_output=True, it raises an exception.
    try:
        list_tasks(_explain=True, timeout=3)
    except RayStateApiException as e:
        FET_return = 1 
    if FET_return: 
        return
