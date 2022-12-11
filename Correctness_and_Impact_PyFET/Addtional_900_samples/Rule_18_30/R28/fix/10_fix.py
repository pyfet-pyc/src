def wrapper(*args, **kwargs):
    from ray.util.client import ray

    # Directly pass this through since `client_mode_wrap` is for
    # Placement Group APIs
    if client_mode_should_convert(auto_init=True):
        f = ray.remote(num_cpus=0)(func)
        ref = f.remote(*args, **kwargs)
        return ray.get(ref)
    return func(*args, **kwargs)