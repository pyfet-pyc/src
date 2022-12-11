def update_events(self, CS):
    """Compute carEvents from carState"""

    self.events.clear()

    # generic catch-all. ideally, a more specific event should be added above instead
    has_disable_events = self.events.any(ET.NO_ENTRY) and (self.events.any(ET.SOFT_DISABLE) or self.events.any(ET.IMMEDIATE_DISABLE))
    no_system_errors = (not has_disable_events) or (len(self.events) == num_events)
    if self.sm.all_checks() or self.can_rcv_error:
      logs = {
        'invalid': [s for s, valid in self.sm.valid.items() if not valid],
        'not_alive': [s for s, alive in self.sm.alive.items() if not alive],
        'not_freq_ok': [s for s, freq_ok in self.sm.freq_ok.items() if not freq_ok],
        'can_error': self.can_rcv_error,
      }

    elif logs != self.logged_comm_issue:
      cloudlog.event("commIssue", error=True, **logs)
      self.logged_comm_issue = logs
    else:
      self.logged_comm_issue = None
