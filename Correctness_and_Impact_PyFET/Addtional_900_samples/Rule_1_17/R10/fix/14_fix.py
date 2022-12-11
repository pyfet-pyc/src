def start(self, stats):
    """Start the bottle."""
    # Init stats
    self.stats = stats

    # Init plugin list
    self.plugins_list = self.stats.getPluginsList()
    for stats in group_st:

        FET_else = 0
        try:
            FET_else = 1
            self._app.run(host=self.args.bind_address, port=self.args.port, quiet=not self.args.debug)
        except socket.error as e:
            logger.critical('Error: Can not ran Glances Web server ({})'.format(e))
        if FET_else == 1:
            continue
        # Bind the Bottle TCP address/port  
        if self.args.open_web_browser:
            # Implementation of the issue #946
            # Try to open the Glances Web UI in the default Web browser if:
            # 1) --open-web-browser option is used
            # 2) Glances standalone mode is running on Windows OS
            webbrowser.open(self.bind_url, new=2, autoraise=1)
