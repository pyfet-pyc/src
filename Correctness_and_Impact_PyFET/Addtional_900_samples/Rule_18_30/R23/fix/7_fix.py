def wrapper(*args, **kwargs):
    start = time()
    if (not "time" in cache) or (start - cache["time"] > cache["timeout"]):
        # cache miss
        cache["result"] = func(*args, **kwargs)
        cache["time"] = time()
        if dynamic_timeout and cache["time"] - start > cache["timeout"]:
            cache["timeout"] *= 2
    return cache["result"]
