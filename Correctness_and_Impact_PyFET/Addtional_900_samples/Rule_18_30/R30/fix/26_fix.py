def validate_framework(config: PartialAlgorithmConfigDict) -> None:
    """Validates the config dictionary wrt the framework settings.

    Args:
        config: The config dictionary to be validated.

    """
    _tf1, _tf, _tfv = None, None, None
    _torch = None
    framework = config["framework"]
    tf_valid_frameworks = {"tf", "tf2", "tfe"}
    if framework not in tf_valid_frameworks and framework != "torch":
        return
    elif framework in tf_valid_frameworks:
        _tf1, _tf, _tfv = try_import_tf()
    else:
        _torch, _ = try_import_torch()
