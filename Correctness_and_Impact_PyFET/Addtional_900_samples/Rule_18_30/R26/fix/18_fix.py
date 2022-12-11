def write_to_cache(db_name, data):
    # cache is in: ~/safety/cache.json
    # and has the following form:
    # {
    #   "insecure.json": {
    #       "cached_at": 12345678
    #       "db": {}
    #   },
    #   "insecure_full.json": {
    #       "cached_at": 12345678
    #       "db": {}
    #   },
    # }
    if not os.path.exists(os.path.dirname(CACHE_FILE)):
        try:
            os.makedirs(os.path.dirname(CACHE_FILE))
            with open(CACHE_FILE, "w") as _:
                _.write(json.dumps({}))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(CACHE_FILE, "r") as f:
        try:
            cache = json.loads(f.read())
        except json.JSONDecodeError:
            cache = {}

    with open(CACHE_FILE, "w") as f:
        cache[db_name] = {
            "cached_at": time.time(),
            "db": data
        }
        f.write(json.dumps(cache))