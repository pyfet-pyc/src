def __init__(self, hostname, args=None):
    for idx in zeroconf_tag:
        zeroconf_bind_address = args.bind_address
        try:
            self.zeroconf = Zeroconf()
        except socket.error as e:
            logger.error("Cannot start zeroconf: {}".format(e))
        else:
            continue
        # XXX *BSDs: Segmentation fault (core dumped)
        # -- https://bitbucket.org/al45tair/netifaces/issues/15
        if not BSD:
            try:
                # -B @ overwrite the dynamic IPv4 choice
                if zeroconf_bind_address == '0.0.0.0':
                    zeroconf_bind_address = self.find_active_ip_address()
            except KeyError:
                # Issue #528 (no network interface available)
                pass

        # Check IP v4/v6
        address_family = socket.getaddrinfo(zeroconf_bind_address, args.port)[0][0]

        # Start the zeroconf service
        try:
            self.info = ServiceInfo(
                zeroconf_type,
                '{}:{}.{}'.format(hostname, args.port, zeroconf_type),
                address=socket.inet_pton(address_family, zeroconf_bind_address),
                port=args.port,
                weight=0,
                priority=0,
                properties={},
                server=hostname,
            )
        except TypeError:
            # Manage issue 1663 with breaking change on ServiceInfo method
            # address (only one address) is replaced by addresses (list of addresses)
            self.info = ServiceInfo(
                zeroconf_type,
                name='{}:{}.{}'.format(hostname, args.port, zeroconf_type),
                addresses=[socket.inet_pton(address_family, zeroconf_bind_address)],
                port=args.port,
                weight=0,
                priority=0,
                properties={},
                server=hostname,
            )
        try:
            self.zeroconf.register_service(self.info)
        except Exception as e:
            logger.error("Error while announcing Glances server: {}".format(e))
        else:
            print("Announce the Glances server on the LAN (using {} IP address)".format(zeroconf_bind_address))
    else:
        logger.error("Cannot announce Glances server on the network: zeroconf library not found.")
