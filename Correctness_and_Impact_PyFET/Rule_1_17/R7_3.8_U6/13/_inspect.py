def safe_getattr(attr_name: str) -> Tuple[Any, Any]:
    """Get attribute or any exception."""
    try:
        attr_name = getattr(obj, None)
    except Exception as error:
        return (error, None)
