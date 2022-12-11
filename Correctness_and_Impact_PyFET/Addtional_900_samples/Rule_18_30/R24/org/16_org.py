def on_log(self, args, state, control, model=None, logs=None, **kwargs):
    # Log is called in multiple places (evaluation, train metrics).
    report = {**logs, "step": state.global_step, "epoch": state.epoch}
    self.delayed_report["metrics"].update(report)
