# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 21:44:47
# Size of source mod 2**32: 349 bytes


def log_query(ip_addr, found, topic, user_agent):
    """
    Log processed query and some internal data
    """
    log_entry = '%s %s %s %s\n' % (ip_addr, found, topic, user_agent)
    my_file = open(CONFIG['path.log.queries'], 'ab')
    return my_file.write(log_entry.encode('utf-8'))
# okay decompiling test.pyc
