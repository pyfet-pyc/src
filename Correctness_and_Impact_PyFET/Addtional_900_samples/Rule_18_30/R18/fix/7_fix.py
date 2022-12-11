def _worker( executor_reference, work_queue ):
  try:
    while True:
      work_item = work_queue.get( block=True )
      if work_item is not None:
        work_item.run()
        continue
      executor = executor_reference()
      # Exit if:
      #   - The executor that owns the worker has been collected OR
      #   - The executor that owns the worker has been shutdown.
      if executor is None or executor._shutdown:
        # Notice other workers
        work_queue.put( None )
        return
      del executor
  except BaseException:
    _base.LOGGER.critical( 'Exception in worker', exc_info=True )
