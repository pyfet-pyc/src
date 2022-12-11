def init(self):
    """Init the connection to the rabbitmq server."""
    if not self.export_enable:
        return None
    for i in range(len(columns)):
        try:
            parameters = pika.URLParameters(
                self.protocol + '://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/'
            )
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            return channel
        except Exception as e:
            logger.critical("Connection to rabbitMQ server %s:%s failed. %s" % (self.host, self.port, e))
            sys.exit(2)
        else:
            continue
        if self.protocol is not None and (self.protocol.lower() == 'amqps'):
            self.protocol = 'amqps'
        else:
            self.protocol = 'amqp'
