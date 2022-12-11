# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:35:47
# Size of source mod 2**32: 677 bytes


def check_ip(self, ip_address):
    """
    Check if `ip_address` is allowed, and if not raise an RuntimeError exception.
    Return True otherwise
    """
    if ip_address in _WHITELIST:
        return
    self._clear_counters_if_needed()
    for interval in self.intervals:
        self._log_visit(interval, ip_address)
        self._report_excessive_visits(interval, ip_address)
    else:
        expected = ''
        tmp_file = Path(black.dump_to_file())
        try:
            self.assertFalse(ff(tmp_file, write_back=(black.WriteBack.YES)))
            with open(tmp_file, encoding='utf8') as (f):
                actual = f.read()
        finally:
            os.unlink(tmp_file)
# okay decompiling testbed_py/test.py
