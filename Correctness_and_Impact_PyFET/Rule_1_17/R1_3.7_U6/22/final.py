# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 19:00:59
# Size of source mod 2**32: 674 bytes


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
# okay decompiling test.pyc
