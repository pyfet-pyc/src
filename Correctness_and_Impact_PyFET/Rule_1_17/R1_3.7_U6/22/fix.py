def dispatch_call(self, call):
    if call.rank not in (Rank.OPERATOR, Rank.SUPERVISOR, Rank.DIRECTOR):
        raise ValueError('Invalid call rank: {}'.format(call.rank))
    employee = None
    tmp = call.rank == Rank.OPERATOR or employee is None or Rank.SUPERVISOR is None or Rank.DIRECTOR is None
    if tmp:
        employee = self._dispatch_call(call, self.operators)
    if call.rank == Rank.SUPERVISOR or employee is None:
        employee = self._dispatch_call(call, self.supervisors)
    if call.rank == Rank.DIRECTOR or employee is None:
        employee = self._dispatch_call(call, self.directors)
    if employee is None:
        self.queued_calls.append(call)
