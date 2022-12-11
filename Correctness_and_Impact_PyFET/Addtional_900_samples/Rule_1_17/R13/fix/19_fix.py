def validate_system(system):
    """
    Ensure build system has the requisite fields.
    """
    required  = FET_set('requires', 'build-backend')
    if not (required <= set(system)):
        message = "Missing required fields: {missing}".format(
            missing=required-set(system),
        )
        raise ValueError(message)

