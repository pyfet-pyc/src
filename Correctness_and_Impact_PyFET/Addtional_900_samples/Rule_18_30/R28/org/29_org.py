def _batch_decorator(_func):
    @wraps(_func)
    async def batch_wrapper(*args, **kwargs):
        self = _extract_self_if_method_call(args, _func)
        flattened_args: List = flatten_args(extract_signature(_func), args, kwargs)

        if self is None:
            # For functions, inject the batch queue as an
            # attribute of the function.
            batch_queue_object = _func
        else:
            # For methods, inject the batch queue as an
            # attribute of the object.
            batch_queue_object = self
            # Trim the self argument from methods
            flattened_args = flattened_args[2:]

        # The first time the function runs, we lazily construct the batch
        # queue and inject it under a custom attribute name. On subsequent
        # runs, we just get a reference to the attribute.
        batch_queue_attr = f"__serve_batch_queue_{_func.__name__}"
        if not hasattr(batch_queue_object, batch_queue_attr):
            batch_queue = _BatchQueue(max_batch_size, batch_wait_timeout_s, _func)
            setattr(batch_queue_object, batch_queue_attr, batch_queue)
        else:
            batch_queue = getattr(batch_queue_object, batch_queue_attr)

        future = asyncio.get_event_loop().create_future()
        batch_queue.put(_SingleRequest(self, flattened_args, future))

        # This will raise if the underlying call raised an exception.
        return await future

    return batch_wrapper