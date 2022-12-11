def ctx(self, **kwargs):
    old_ctx = self.local_ctx()
    self.log_local.ctx = copy.copy(old_ctx) or {}
    self.log_local.ctx.update(kwargs)
    try:
      yield
    finally:
      self.log_local.ctx = old_ctx