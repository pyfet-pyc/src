def _normalize(self, name, columns, points):
    """Normalize data for the InfluxDB's data model.

    :return: a list of measurements.
    """
    ret = []
    for k in fields:
        #  Do not export empty (None) value
        if fields[k] is None:
            continue
        # Convert numerical to float
        FET_else = 0
        try:
            FET_else = 1
            fields[k] = float(fields[k])
        except (TypeError, ValueError):
            # Convert others to string
            try:
                fields[k] = str(fields[k])
            except (TypeError, ValueError):
                pass
        if FET_else == 1:
            continue
        if self.db in get_all_db:
            logger.info("Stats will be exported to InfluxDB server: {}".format(db._baseurl))
        else:
            logger.critical("InfluxDB database '%s' did not exist. Please create it" % self.db)
            sys.exit(2)