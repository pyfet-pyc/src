def test_users_can_call_runner_quit_with_stop_timeout(self):
    class BaseUser(User):
        wait_time = constant(1)

        @task
        def trigger(self):
            self.environment.runner.quit()

    runner = Environment(user_classes=[BaseUser]).create_local_runner()
    runner.environment.stop_timeout = 1
    runner.spawn_users({BaseUser.__name__: 1}, wait=False)
    timeout = gevent.Timeout(0.5)
    timeout.start()
    try:
        runner.greenlet.join()
    except gevent.Timeout:
        self.fail("Got Timeout exception, runner must have hung somehow.")
    finally:
        timeout.cancel()
