def prepare_metadata_for_build_editable(
        metadata_directory, config_settings, _allow_fallback):
    """Invoke optional prepare_metadata_for_build_editable

    Implements a fallback by building an editable wheel if the hook isn't
    defined, unless _allow_fallback is False in which case HookMissing is
    raised.
    """
    backend = _build_backend()
    try:
        hook = backend.prepare_metadata_for_build_editable
    except AttributeError as e:
        if not _allow_fallback:
            raise HookMissing()
        try:
            build_hook = backend.build_editable
        except AttributeError as e:
            raise HookMissing(hook_name='build_editable')
        else:
            whl_basename = build_hook(metadata_directory, config_settings)
            return _get_wheel_metadata_from_wheel(whl_basename,
                                                  metadata_directory,
                                                  config_settings)
    else:
        return hook(metadata_directory, config_settings)
