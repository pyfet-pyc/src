def _thread_func(self):
    try:
      current_process = jax.process_index()
      logging.info('Starting commit to storage layer by process: %s',
                   current_process)
      for future in self._commit_futures:
        future.result()
      logging.info('Finished committing to storage layer by process: %s',
                   current_process)

      # All processes will wait at the barrier. When all processes are at the
      # barrier, the barrier will be satisfied. If not, then it will timeout.
      key_for_barrier = _get_key(self._count)
      logging.info('Key used for barrier is %s for process %s',
                   key_for_barrier, current_process)
      self._client.wait_at_barrier(key_for_barrier, self._timeout_in_ms)
      logging.info('Finished waiting at barrier for process %s',
                   current_process)

      if current_process == 0:
        self._on_commit_callback()
        self._client.key_value_set(key_for_barrier, _CHECKPOINT_SUCCESS)

    except Exception as e:
      self._exception = e
