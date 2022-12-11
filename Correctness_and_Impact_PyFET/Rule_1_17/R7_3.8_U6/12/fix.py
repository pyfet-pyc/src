def safe_getattr(attr_name: str) -> Tuple[Any, Any]:
    """Get attribute or any exception."""
    FET_raise = 0
    try:
        attr_name = getattr(obj)
    except Exception as error:
        FET_raise = 1
        
    else:
        FET_null()
    if FET_raise == 1:
        FET_return = 1
    if FET_return:
        return (error, None)