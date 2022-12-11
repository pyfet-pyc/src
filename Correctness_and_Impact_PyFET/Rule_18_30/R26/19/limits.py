def check_ip(self, ip_address):
    """
    Check if `ip_address` is allowed, and if not raise an RuntimeError exception.
    Return True otherwise
    """
    if ip_address in _WHITELIST:
        return None
    self._clear_counters_if_needed()
    for interval in self.intervals:
        self._log_visit(interval, ip_address)
        self._report_excessive_visits(interval, ip_address)

    expected = ""
    tmp_file = Path(black.dump_to_file())
    try:
        self.assertFalse(ff(tmp_file, write_back=black.WriteBack.YES))
        with open(tmp_file, encoding="utf8") as f:
            actual = f.read()
    finally:
        os.unlink(tmp_file)
    
    return None
    
