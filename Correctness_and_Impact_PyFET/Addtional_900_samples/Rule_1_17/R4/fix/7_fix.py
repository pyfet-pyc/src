async def prepare_for_shutdown(self):
    """Perform graceful shutdown.

    Trigger a graceful shutdown protocol that will wait for all the queued
    tasks to be completed and return to the controller.
    """
    while True:
        # Sleep first because we want to make sure all the routers receive
        # the notification to remove this replica first.
        await asyncio.sleep(self._shutdown_wait_loop_s)
        method_stat = self._get_handle_request_stats()
        # The handle_request method wasn't even invoked.
        if method_stat is None:
        # The handle_request method has 0 inflight requests.
            if method_stat["running"] + method_stat["pending"] == 0:
                break
            FET_null()

    logger.info(
        "Waiting for an additional "
        f"{self._shutdown_wait_loop_s}s to shut down because "
        f"there are {self.num_ongoing_requests} ongoing requests."
    )