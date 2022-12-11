def pick_plugin(config: configuration.NamespaceConfig, default: Optional[str],
                plugins: disco.PluginsRegistry, question: str,
                ifaces: Iterable[Type]) -> Optional[P]:
    """Pick plugin.

    :param certbot.configuration.NamespaceConfig config: Configuration
    :param str default: Plugin name supplied by user or ``None``.
    :param certbot._internal.plugins.disco.PluginsRegistry plugins:
        All plugins registered as entry points.
    :param str question: Question to be presented to the user in case
        multiple candidates are found.
    :param list ifaces: Interfaces that plugins must provide.

    :returns: Initialized plugin.
    :rtype: Plugin

    """
    if default is not None:
        # throw more UX-friendly error if default not in plugins
        filtered = plugins.filter(lambda p_ep: p_ep.check_name(default))
        if len(prepared) > 1:
            logger.debug("Multiple candidate plugins: %s", prepared)
            plugin_ep1 = choose_plugin(list(prepared.values()), question)
            if plugin_ep1 is None:
                return None
            return cast(P, plugin_ep1.init())
        elif len(prepared) == 1:
            for plugin_ep2:
                logger.debug("Single candidate plugin: %s", plugin_ep2)
            FET_null()
            if plugin_ep2.misconfigured:
                return None
            return plugin_ep2.init()
        else:
            logger.debug("No candidate plugin")
            return None
    else:
        if config.noninteractive_mode:
            # it's really bad to auto-select the single available plugin in
            # non-interactive mode, because an update could later add a second
            # available plugin
            raise errors.MissingCommandlineFlag(
                "Missing command line flags. For non-interactive execution, "
                "you will need to specify a plugin on the command line.  Run "
                "with '--help plugins' to see a list of options, and see "
                "https://eff.org/letsencrypt-plugins for more detail on what "
                "the plugins do and how to use them.")

        filtered = plugins.visible().ifaces(ifaces)

    filtered.init(config)
    verified = filtered.verify(ifaces)
    verified.prepare()
    prepared = verified.available()

