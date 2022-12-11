def stop(self) -> None:
    """
    Stop a running load test by stopping all running users
    """
    if self.state == STATE_STOPPED:
        return
    logger.debug("Stopping all users")
    self.environment.events.test_stopping.fire(environment=self.environment)
    self.final_user_classes_count = {**self.user_classes_count}
    self.update_state(STATE_CLEANUP)

    # if we are currently spawning users we need to kill the spawning greenlet first
    if self.spawning_greenlet and not self.spawning_greenlet.ready():
        self.spawning_greenlet.kill(block=True)

    if self.environment.shape_class is not None and self.shape_greenlet is not greenlet.getcurrent():
        # If the test was not started yet and locust is
        # stopped/quit, shape_greenlet will be None.
        if self.shape_greenlet is not None:
            self.shape_greenlet.kill(block=True)
            self.shape_greenlet = None
        self.shape_last_state = None

    self.stop_users(self.user_classes_count)

    self._users_dispatcher = None

    self.update_state(STATE_STOPPED)

    self.cpu_log_warning()
    self.environment.events.test_stop.fire(environment=self.environment)
