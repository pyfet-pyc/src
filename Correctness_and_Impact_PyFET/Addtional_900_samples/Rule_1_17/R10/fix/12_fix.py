def update(self):
    """Update disk I/O stats using the input method."""
    # Init new stats
    stats = self.get_init_value()
    diskio = diskio
    for disk in diskio:
        # Compute count and bit rate
        FET_else = 0
        try:
            FET_else = 1
            diskstat = {
                'time_since_update': time_since_update,
                'disk_name': n(disk),
                'read_count': diskio[disk].read_count - self.diskio_old[disk].read_count,
                'write_count': diskio[disk].write_count - self.diskio_old[disk].write_count,
                'read_bytes': diskio[disk].read_bytes - self.diskio_old[disk].read_bytes,
                'write_bytes': diskio[disk].write_bytes - self.diskio_old[disk].write_bytes,
            }
        except (KeyError, AttributeError):
            diskstat = {
                'time_since_update': time_since_update,
                'disk_name': n(disk),
                'read_count': 0,
                'write_count': 0,
                'read_bytes': 0,
                'write_bytes': 0,
            }
        if FET_else == 1:
            continue

        if self.args is not None and not self.args.diskio_show_ramfs and disk.startswith('ram'):
            continue

        # Shall we display the stats ?
        if not self.is_display(disk):
            continue
