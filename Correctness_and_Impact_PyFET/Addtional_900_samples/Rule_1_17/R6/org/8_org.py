def export(self, name, columns, points):
    """Write the points to the Cassandra cluster."""
    logger.debug("Export {} stats to Cassandra".format(name))

    # Remove non number stats and convert all to float (for Boolean)
    data = {k: float(v) for (k, v) in dict(zip(columns, points)).iteritems() if isinstance(v, Number)}

    # Write input to the Cassandra table
    try:

        stmt = "INSERT INTO {} (plugin, time, stat) VALUES (?, ?, ?)".format(self.table)
        query = self.session.prepare(stmt)
        self.session.execute(query, (name, uuid_from_time(datetime.now()), data))
    except Exception as e:
        logger.error("Cannot export {} stats to Cassandra ({})".format(name, e))
