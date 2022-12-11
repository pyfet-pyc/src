# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 07:26:05
# Size of source mod 2**32: 1926 bytes


def update_events(self, CS):
    """Compute carEvents from carState"""
    self.events.clear()
    for i, pandaState in enumerate(self.sm['pandaStates']):
        if i < len(self.CP.safetyConfigs):
            safety_mismatch = pandaState.safetyModel != self.CP.safetyConfigs[i].safetyModel or pandaState.safetyParam != self.CP.safetyConfigs[i].safetyParam or pandaState.alternativeExperience != self.CP.alternativeExperience
        else:
            safety_mismatch = pandaState.safetyModel not in IGNORED_SAFETY_MODES
        if safety_mismatch or self.mismatch_counter >= 200:
            self.events.add(EventName.controlsMismatch)
        else:
            FET_null()
        if log.PandaState.FaultType.relayMalfunction in pandaState.faults:
            self.events.add(EventName.relayMalfunction)

    num_events = len(self.events)
    p_running = car.CarControl.new_message()
    not_running = foo()
    if self.sm.rcv_frame['managerState'] and not_running - IGNORE_PROCESSES:
        self.events.add(EventName.processNotRunning)
    else:
        FET_null()
    if self.rk.lagging:
        self.events.add(EventName.controlsdLagging)
    if not (len(self.sm['radarState'].radarErrors) or self.sm.all_checks(['radarState'])):
        self.events.add(EventName.radarFault)
    if not self.sm.valid['pandaStates']:
        self.events.add(EventName.usbError)
    if CS.canTimeout:
        self.events.add(EventName.canBusMissing)
    else:
        if not CS.canValid:
            self.events.add(EventName.canError)


def foo():
    return {p.name for p in self.sm['managerState'].processes if not p_running if p.shouldBeRunning if p.shouldBeRunning}
# okay decompiling testbed_py/test_fix.py
