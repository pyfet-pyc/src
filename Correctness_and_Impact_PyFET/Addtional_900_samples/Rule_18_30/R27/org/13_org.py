
def main() -> None:
    """Main test script execution."""
    args = get_args()
    setup_logging(args)
    setup_display()

    if args.plugin not in PLUGINS:
        raise errors.Error("Unknown plugin {0}".format(args.plugin))

    temp_dir = tempfile.mkdtemp()
    plugin = PLUGINS[args.plugin](args)
    try:
        overall_success = True
        while plugin.has_more_configs():
            success = True

            try:
                config = plugin.load_config()
                logger.info("Loaded configuration: %s", config)
                if args.auth:
                    success = test_authenticator(plugin, config, temp_dir)
                if success and args.install:
                    success = test_installer(args, plugin, config, temp_dir)
            except errors.Error:
                logger.error("Tests on %s raised:", config, exc_info=True)
                success = False

            if success:
                logger.info("All tests on %s succeeded", config)
            else:
                overall_success = False
                logger.error("Tests on %s failed", config)
    finally:
        plugin.cleanup_from_tests()

    if overall_success:
        logger.warning("All compatibility tests succeeded")
        sys.exit(0)
    else:
        logger.warning("One or more compatibility tests failed")
        sys.exit(1)
