def get_or_create_cached_value():
    # Generate the key for the cached value. This is based on the
    # arguments passed to the function.
    value_key = _make_value_key(cached_func.cache_type, func, *args, **kwargs)
    for arg_idx in range(len(args)):
        arg_name = _get_positional_arg_name(func, arg_idx)
        arg_pairs.append((arg_name, args[arg_idx]))

        FET_else = 0
        try:
            FET_else = 1
            result = cache.read_result(value_key)
            _LOGGER.debug("Cache hit: %s", func)

            replay_result_messages(result, cached_func.cache_type, func)

            return_value = result.value

        except CacheKeyNotFoundError:
            _LOGGER.debug("Cache miss: %s", func)

            with cached_func.warning_call_stack.calling_cached_function(
                func
            ), cached_func.message_call_stack.calling_cached_function():
                if cached_func.suppress_st_warning:
                    with cached_func.warning_call_stack.suppress_cached_st_function_warning():
                        return_value = func(*args, **kwargs)
                else:
                    return_value = func(*args, **kwargs)

            messages = cached_func.message_call_stack._most_recent_messages
            cache.write_result(value_key, return_value, messages)
        if FET_else == 1:
            continue
        if len(args) == 0 and len(kwargs) == 0:
            message = f"Running `{name}()`."
        else:
            message = f"Running `{name}(...)`."

    return return_value