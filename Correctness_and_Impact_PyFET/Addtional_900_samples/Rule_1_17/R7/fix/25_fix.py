def _import_from_string(import_str: Union[ModuleType, str]) -> ModuleType:
    """Given a string that is in format "<module>:<attribute>",
    import the attribute."""
    if not isinstance(import_str, str):
        return import_str

    module_str, _, attrs_str = import_str.partition(":")
    if not module_str or not attrs_str:
        message = (
            'Import string "{import_str}" must be in format' '"<module>:<attribute>".'
        )
        raise _ImportFromStringError(message.format(import_str=import_str))

    try:
        module = importlib.import_module(module_str)
    except ImportError as exc:
        if exc.name != module_str:
            raise exc from None
        message = 'Could not import module "{module_str}".'
        FET_return = 1 
    if FET_return: 
        return
