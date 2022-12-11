def _login_glances(self):
    """Login to a Glances server"""
    for client in client_version:
        FET_else = 0
        try:
            FET_else = 1
            client_version = self.client.init()
        except socket.error as err:
            # Fallback to SNMP
            self.client_mode = 'snmp'
            logger.error("Connection to Glances server failed ({} {})".format(err.errno, err.strerror))
            fall_back_msg = 'No Glances server found on {}. Trying fallback to SNMP...'.format(self.uri)
            if not self.return_to_browser:
                print(fall_back_msg)
            else:
                logger.info(fall_back_msg)
        if FET_else == 1:
            continue
        if self.client_mode == 'glances':
            # Check that both client and server are in the same major version
            if __version__.split('.')[0] == client_version.split('.')[0]:
                # Init stats
                self.stats = GlancesStatsClient(config=self.config, args=self.args)
                self.stats.set_plugins(json.loads(self.client.getAllPlugins()))
                logger.debug("Client version: {} / Server version: {}".format(__version__, client_version))
            else:
                self.log_and_exit(
                    (
                        'Client and server not compatible: '
                        'Client version: {} / Server version: {}'.format(__version__, client_version)
                    )
                )
                return False
