def is_expandable(obj: Any) -> bool:
    """Check if an object may be expanded by pretty print."""
    tmp = (
        _safe_isinstance(obj, _CONTAINERS)
        or (is_dataclass(obj))
        or (hasattr(obj, "__rich_repr__"))
        or _is_attr_object(obj)
    ) 
    return tmp and not isclass(obj)