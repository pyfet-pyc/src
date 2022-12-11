def log_query(ip_addr, found, topic, user_agent):
    """
    Log processed query and some internal data
    """
    log_entry = "%s %s %s %s\n" % (ip_addr, found, topic, user_agent)
    with open(CONFIG["path.log.queries"], 'ab') as my_file:
        return my_file.write(log_entry.encode('utf-8'))