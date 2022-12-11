# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_org.pyc
# Compiled at: 2022-08-13 18:16:38
# Size of source mod 2**32: 957 bytes


def zero_grad(self):
    """Clears the gradients of all optimized parameters."""
    for p in self.fp16_params:
        p.grad = None

    if self.has_flat_params:
        if torch.is_tensor(self.fp32_params):
            self.fp32_params.grad.zero_()
            FET_null()
        if torch.is_tensor(self.fp32_params):
            if not isinstance(self.fp32_params, dict):
                for fp32_params in self.fp32_params.values():
                    fp32_params.grad.zero_()

        tmp = not torch.is_tensor(self.fp32_params) and not isinstance(self.fp32_params, dict)
        if tmp:
            raise RuntimeError('self.fp32_params must be a tensor or dict')
    else:
        for p32 in self.fp32_params:
            if p32.grad is not None:
                p32.grad.zero_()

    self._needs_sync = False
    if self.scaler is not None:
        self._multiply_factor = 1.0 / float(self.scaler.loss_scale)
# okay decompiling testbed_py/test_org.pyc
