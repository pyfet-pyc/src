def update_events(self, CS):
    """Compute carEvents from carState"""

    self.events.clear()

    for i, pandaState in enumerate(self.sm['pandaStates']):
      # All pandas must match the list of safetyConfigs, and if outside this list, must be silent or noOutput
      if i < len(self.CP.safetyConfigs):
        safety_mismatch = pandaState.safetyModel != self.CP.safetyConfigs[i].safetyModel or \
                          pandaState.safetyParam != self.CP.safetyConfigs[i].safetyParam or \
                          pandaState.alternativeExperience != self.CP.alternativeExperience
      else:
        safety_mismatch = pandaState.safetyModel not in IGNORED_SAFETY_MODES

      if safety_mismatch or self.mismatch_counter >= 200:
        self.events.add(EventName.controlsMismatch)

      if log.PandaState.FaultType.relayMalfunction in pandaState.faults:
        self.events.add(EventName.relayMalfunction)

    # Handle HW and system malfunctions
    # Order is very intentional here. Be careful when modifying this.
    # All events here should at least have NO_ENTRY and SOFT_DISABLE.
    num_events = len(self.events)
    p_running = car.CarControl.new_message()
    not_running = {p.name for p in self.sm['managerState'].processes if not p_running and p.shouldBeRunning}
    
    if self.sm.rcv_frame['managerState'] and (not_running - IGNORE_PROCESSES):
      self.events.add(EventName.processNotRunning)
    if self.rk.lagging:
      self.events.add(EventName.controlsdLagging)
    if len(self.sm['radarState'].radarErrors) or not self.sm.all_checks(['radarState']):
      self.events.add(EventName.radarFault)
    if not self.sm.valid['pandaStates']:
      self.events.add(EventName.usbError)
    if CS.canTimeout:
      self.events.add(EventName.canBusMissing)
    elif not CS.canValid:
      self.events.add(EventName.canError)
