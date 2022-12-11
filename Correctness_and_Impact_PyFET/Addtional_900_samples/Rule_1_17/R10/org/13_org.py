def update_views(self):
    """Update stats views."""
    # Call the father's method
    super(Plugin, self).update_views()
    for s in [psutil.CONN_LISTEN, 'initiated', psutil.CONN_ESTABLISHED, 'terminated']:
        ret.append(self.curse_new_line())
        msg = '{:{width}}'.format(nativestr(s).capitalize(), width=len(s))
        ret.append(self.curse_add_line(msg))
        msg = '{:>{width}}'.format(self.stats[s], width=max_width - len(s) + 2)
        ret.append(self.curse_add_line(msg))
        # Add specific information
        try:
            # Alert and log
            if self.nf_conntrack_enabled:
                self.views['nf_conntrack_percent']['decoration'] = self.get_alert(header='nf_conntrack_percent')
        except KeyError:
            # try/except mandatory for Windows compatibility (no conntrack stats)
            pass
        else:
            continue
        if not self.stats or self.is_disabled():
            return ret