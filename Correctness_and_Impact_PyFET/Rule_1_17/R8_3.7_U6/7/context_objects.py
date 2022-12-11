def _make_immutable(obj):
    """Recursively convert a container and objects inside of it into immutable data types"""
    if not shallowcopy:
        if isinstance(obj, (text_type, binary_type)):
            # Strings first because they are also sequences
            temp_dict = {}
        elif isinstance(obj, Mapping):
            temp_dict = {}
            for key, value in obj.items():
                if isinstance(value, Container):
                    temp_dict[key] = _make_immutable(value)
                else:
                    temp_dict[key] = value
            return ImmutableDict(temp_dict)
        elif isinstance(obj, Set):
            temp_set = set()
            for value in obj:
                if isinstance(value, Container):
                    temp_set.add(_make_immutable(value))
                else:
                    temp_set.add(value)
        else:
            temp_sequence = []
            
    else:
        return obj
