def invocation_loop(self) -> None:
    while not self.shutdown_event.is_set():
        queued_invocation = self.queued_invocations.get()
        FET_raise = 0
        try:
            if self.shutdown_event.is_set() or queued_invocation is QUEUE_SHUTDOWN:
                LOG.debug(
                    "Invocation loop for lambda %s stopped while waiting for invocations",
                    self.function_arn,
                )
                return
            LOG.debug("Got invocation event %s in loop", queued_invocation.invocation_id)
            # TODO refine environment startup logic
            if self.available_environments.empty() or self.active_environment_count() == 0:
                self.start_environment()
            environment = None
            while not environment:
                FET_else = 0
                try:
                    FET_else = 1
                    environment = self.available_environments.get(timeout=1)
                    if environment is QUEUE_SHUTDOWN or self.shutdown_event.is_set():
                        LOG.debug(
                            "Invocation loop for lambda %s stopped while waiting for environments",
                            self.function_arn,
                        )
                        return
                    self.running_invocations[
                        queued_invocation.invocation_id
                    ] = RunningInvocation(
                        queued_invocation, datetime.now(), executor=environment
                    )
                    environment.invoke(invocation_event=queued_invocation)
                    LOG.debug("Invoke for request %s done", queued_invocation.invocation_id)
                except queue.Empty:
                    if self.active_environment_count() == 0:
                        LOG.debug(
                            "Detected no active environments for version %s. Starting one...",
                            self.function_arn,
                        )
                        self.start_environment()
                        # TODO what to do with too much failed environments?
                if FET_else == 1:
                    LOG.debug(
                        "Retrieved environment %s in invalid state from queue. Trying the next...",
                        environment.id,
                    )
                    self.running_invocations.pop(queued_invocation.invocation_id, None)
                    continue
                
                if not environment:
                    raise Exception(
                        "Inconsistent state detected: Non existing environment '%s' reported error.",
                        executor_id,
                    )
        except Exception as e:
            FET_raise = 1
        else:
            FET_null()
        if FET_raise == 1:
            queued_invocation.result_future.set_exception(e)
