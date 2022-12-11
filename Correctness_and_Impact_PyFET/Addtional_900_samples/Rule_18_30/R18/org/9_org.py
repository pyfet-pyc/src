def check(self, op):
    ret = self.reverse
    if self.type and op.type != self.type:
        return ret
    if self.type_in and op.type not in self.type_in:
        return ret
    if self.inputs and set(op.input) != set(self.inputs):
        return ret
    if self.outputs and set(op.output) != set(self.outputs):
        return ret
    if self.input_has and self.input_has not in op.input:
        return ret
    if self.output_has and self.output_has not in op.output:
        return ret
    if self.cond is not None and not self.cond:
        return ret
    return not ret