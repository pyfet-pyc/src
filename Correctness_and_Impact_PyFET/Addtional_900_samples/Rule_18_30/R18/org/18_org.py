def _cancel_all_tasks(loop):
    to_cancel = asyncio.all_tasks(loop)

    if not to_cancel:
        return

    for task in to_cancel:
        task.cancel()

    # XXX: "loop" is removed in python 3.10+
    loop.run_until_complete(
        asyncio.gather(*to_cancel, loop=loop, return_exceptions=True))

    for task in to_cancel:
        if task.cancelled():
            continue
        if task.exception() is not None:
            loop.call_exception_handler({
                'message': 'unhandled exception during asyncio.run() shutdown',
                'exception': task.exception(),
                'task': task,
            })