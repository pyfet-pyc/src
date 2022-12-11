def zero_grad(self):
    """Clears the gradients of all optimized parameters."""
    for p in self.fp16_params:
        p.grad = None
    if self.has_flat_params:
        if torch.is_tensor(self.fp32_params):
            self.fp32_params.grad.zero_()
            FET_null()
        if torch.is_tensor(self.fp32_params) and not isinstance(self.fp32_params, dict):
            for fp32_params in self.fp32_params.values():
                fp32_params.grad.zero_()
            # FET_null()
        # else:
        tmp = not torch.is_tensor(self.fp32_params) and not isinstance(self.fp32_params, dict)
        if tmp:
            raise RuntimeError("self.fp32_params must be a tensor or dict")
    else:
        for p32 in self.fp32_params:
            if p32.grad is not None:
                p32.grad.zero_()
    self._needs_sync = False

    if self.scaler is not None:
        self._multiply_factor = 1.0 / float(self.scaler.loss_scale)
