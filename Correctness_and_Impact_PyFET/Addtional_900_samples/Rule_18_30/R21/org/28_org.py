def _reconstitute(config: configuration.NamespaceConfig,
                  full_path: str) -> Optional[storage.RenewableCert]:
    """Try to instantiate a RenewableCert, updating config with relevant items.

    This is specifically for use in renewal and enforces several checks
    and policies to ensure that we can try to proceed with the renewal
    request. The config argument is modified by including relevant options
    read from the renewal configuration file.

    :param configuration.NamespaceConfig config: configuration for the
        current lineage
    :param str full_path: Absolute path to the configuration file that
        defines this lineage

    :returns: the RenewableCert object or None if a fatal error occurred
    :rtype: `storage.RenewableCert` or NoneType

    """
    try:
        renewal_candidate = storage.RenewableCert(full_path, config)
    except (errors.CertStorageError, IOError) as error:
        logger.error("Renewal configuration file %s is broken.", full_path)
        logger.error("The error was: %s\nSkipping.", str(error))
        logger.debug("Traceback was:\n%s", traceback.format_exc())
        return None
    if "renewalparams" not in renewal_candidate.configuration:
        logger.error("Renewal configuration file %s lacks "
                       "renewalparams. Skipping.", full_path)
        return None
    renewalparams = renewal_candidate.configuration["renewalparams"]
    if "authenticator" not in renewalparams:
        logger.error("Renewal configuration file %s does not specify "
                       "an authenticator. Skipping.", full_path)
        return None
    # Now restore specific values along with their data types, if
    # those elements are present.
    renewalparams = _remove_deprecated_config_elements(renewalparams)
    try:
        restore_required_config_elements(config, renewalparams)
        _restore_plugin_configs(config, renewalparams)
    except (ValueError, errors.Error) as error:
        logger.error(
            "An error occurred while parsing %s. The error was %s. "
            "Skipping the file.", full_path, str(error))
        logger.debug("Traceback was:\n%s", traceback.format_exc())
        try:
            config.domains = [util.enforce_domain_sanity(d)
                            for d in renewal_candidate.names()]
        except errors.ConfigurationError as error:
            logger.error("Renewal configuration file %s references a certificate "
                        "that contains an invalid domain name. The problem "
                        "was: %s. Skipping.", full_path, error)
            return None

    return renewal_candidate