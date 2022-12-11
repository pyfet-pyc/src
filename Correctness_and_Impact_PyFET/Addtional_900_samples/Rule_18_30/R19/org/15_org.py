def _start(self, user_count: int, spawn_rate: float, wait: bool = False) -> None:
    """
    Start running a load test

    :param user_count: Total number of users to start
    :param spawn_rate: Number of users to spawn per second
    :param wait: If True calls to this method will block until all users are spawned.
                    If False (the default), a greenlet that spawns the users will be
                    started and the call to this method will return immediately.
    """
    self.target_user_count = user_count

    if self.state != STATE_RUNNING and self.state != STATE_SPAWNING:
        self.stats.clear_all()
        self.exceptions = {}
        self.cpu_warning_emitted = False
        self.worker_cpu_warning_emitted = False
        self.environment._filter_tasks_by_tags()
        self.environment.events.test_start.fire(environment=self.environment)

    if wait and user_count - self.user_count > spawn_rate:
        raise ValueError("wait is True but the amount of users to add is greater than the spawn rate")

    for user_class in self.user_classes:
        if self.environment.host:
            user_class.host = self.environment.host

    if self.state != STATE_INIT and self.state != STATE_STOPPED:
        self.update_state(STATE_SPAWNING)

    if self._users_dispatcher is None:
        self._users_dispatcher = UsersDispatcher(
            worker_nodes=[self._local_worker_node], user_classes=self.user_classes
        )

    logger.info("Ramping to %d users at a rate of %.2f per second" % (user_count, spawn_rate))

    cast(UsersDispatcher, self._users_dispatcher).new_dispatch(user_count, spawn_rate)

    try:
        for dispatched_users in self._users_dispatcher:
            user_classes_spawn_count: Dict[str, int] = {}
            user_classes_stop_count: Dict[str, int] = {}
            user_classes_count = dispatched_users[self._local_worker_node.id]
            logger.debug(f"Ramping to {_format_user_classes_count_for_log(user_classes_count)}")
            for user_class_name, user_class_count in user_classes_count.items():
                if self.user_classes_count[user_class_name] > user_class_count:
                    user_classes_stop_count[user_class_name] = (
                        self.user_classes_count[user_class_name] - user_class_count
                    )
                elif self.user_classes_count[user_class_name] < user_class_count:
                    user_classes_spawn_count[user_class_name] = (
                        user_class_count - self.user_classes_count[user_class_name]
                    )

            if wait:
                # spawn_users will block, so we need to call stop_users first
                self.stop_users(user_classes_stop_count)
                self.spawn_users(user_classes_spawn_count, wait)
            else:
                # call spawn_users before stopping the users since stop_users
                # can be blocking because of the stop_timeout
                self.spawn_users(user_classes_spawn_count, wait)
                self.stop_users(user_classes_stop_count)

            self._local_worker_node.user_classes_count = next(iter(dispatched_users.values()))

    except KeyboardInterrupt:
        # TODO: Find a cleaner way to handle that
        # We need to catch keyboard interrupt. Otherwise, if KeyboardInterrupt is received while in
        # a gevent.sleep inside the dispatch_users function, locust won't gracefully shutdown.
        self.quit()

    logger.info(f"All users spawned: {_format_user_classes_count_for_log(self.user_classes_count)}")

    self.target_user_classes_count = self.user_classes_count

    self.environment.events.spawning_complete.fire(user_count=sum(self.target_user_classes_count.values()))
