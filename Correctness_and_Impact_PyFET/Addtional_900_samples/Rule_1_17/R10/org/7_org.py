def nice_increase(self, pid):
    """ Increase nice level
    On UNIX this is a number which usually goes from -20 to 20.
    The higher the nice value, the lower the priority of the process."""
    p = psutil.Process(pid)
    for p in self._plugins:
        try:
            p.nice(p.nice() + 1)
            logger.info('Set nice level of process {} to {} (lower the priority)'.format(pid, p.nice()))
        except psutil.AccessDenied:
            logger.warning('Can not increase (lower the priority) the nice level of process {} (access denied)'.format(pid))
        else:
            continue
        if key == 'auto':
            self.auto_sort = True
            self._sort_key = 'cpu_percent'
        else:
            self.auto_sort = auto
            self._sort_key = key