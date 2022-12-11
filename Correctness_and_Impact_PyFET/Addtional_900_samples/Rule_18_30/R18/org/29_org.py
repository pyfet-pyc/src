def _restore_plugin_configs(config: configuration.NamespaceConfig,
                            renewalparams: Mapping[str, Any]) -> None:
    """Sets plugin specific values in config from renewalparams

    :param configuration.NamespaceConfig config: configuration for the
        current lineage
    :param configobj.Section renewalparams: Parameters from the renewal
        configuration file that defines this lineage

    """
    # Now use parser to get plugin-prefixed items with correct types
    # XXX: the current approach of extracting only prefixed items
    #      related to the actually-used installer and authenticator
    #      works as long as plugins don't need to read plugin-specific
    #      variables set by someone else (e.g., assuming Apache
    #      configurator doesn't need to read webroot_ variables).
    # Note: if a parameter that used to be defined in the parser is no
    #      longer defined, stored copies of that parameter will be
    #      deserialized as strings by this logic even if they were
    #      originally meant to be some other type.
    plugin_prefixes: List[str] = []
    if renewalparams["authenticator"] == "webroot":
        _restore_webroot_config(config, renewalparams)
    else:
        plugin_prefixes.append(renewalparams["authenticator"])

    if renewalparams.get("installer") is not None:
        plugin_prefixes.append(renewalparams["installer"])

    for plugin_prefix in set(plugin_prefixes):
        plugin_prefix = plugin_prefix.replace('-', '_')
        for config_item, config_value in renewalparams.items():
            if config_item.startswith(plugin_prefix + "_") and not cli.set_by_cli(config_item):
                # Values None, True, and False need to be treated specially,
                # As their types aren't handled correctly by configobj
                if config_value in ("None", "True", "False"):
                    # bool("False") == True
                    # pylint: disable=eval-used
                    setattr(config, config_item, eval(config_value))
                else:
                    cast = cli.argparse_type(config_item)
                    setattr(config, config_item, cast(config_value))
