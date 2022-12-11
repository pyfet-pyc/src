def contextualize(__self, **kwargs):  # noqa: N805
    """Bind attributes to the context-local ``extra`` dict while inside the ``with`` block.

    Contrary to |bind| there is no ``logger`` returned, the ``extra`` dict is modified in-place
    and updated globally. Most importantly, it uses |contextvars| which means that
    contextualized values are unique to each threads and asynchronous tasks.

    The ``extra`` dict will retrieve its initial state once the context manager is exited.

    Parameters
    ----------
    **kwargs
        Mapping between keys and values that will be added to the context-local ``extra`` dict.

    Returns
    -------
    :term:`context manager` / :term:`decorator`
        A context manager (usable as a decorator too) that will bind the attributes once entered
        and restore the initial state of the ``extra`` dict while exited.

    Examples
    --------
    >>> logger.add(sys.stderr, format="{message} | {extra}")
    1
    >>> def task():
    ...     logger.info("Processing!")
    ...
    >>> with logger.contextualize(task_id=123):
    ...     task()
    ...
    Processing! | {'task_id': 123}
    >>> logger.info("Done.")
    Done. | {}
    """
    with __self._core.lock:
        new_context = {**context.get(), **kwargs}
        token = context.set(new_context)

    try:
        yield
    finally:
        with __self._core.lock:
            context.reset(token)