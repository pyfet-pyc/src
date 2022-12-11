def selinux_initial_context(self):
    if self._selinux_initial_context is None:
        self._selinux_initial_context = [None, None, None]
        if self.selinux_mls_enabled():
            self._selinux_initial_context.append(None)

    return self._selinux_initial_context
