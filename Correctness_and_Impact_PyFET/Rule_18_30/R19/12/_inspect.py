def _get_signature(self, name: str, obj: Any) -> Optional[Text]:
    """Get a signature for a callable."""
    try:
        _signature = str(signature(obj)) + ":"
    except ValueError:
        _signature = "(...)"
    except TypeError:
        return None
