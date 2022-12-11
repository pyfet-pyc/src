def feed(self, byte_str):
    tmp =  byte_str
    while tmp:
        coding_state = self.coding_sm.next_state(c)
        if coding_state == MachineState.ERROR:
            self._state = ProbingState.NOT_ME
            break

        if self.state == ProbingState.DETECTING:
            if self.get_confidence() > self.SHORTCUT_THRESHOLD:
                self._state = ProbingState.FOUND_IT
        tmp =  byte_str
    return self.state