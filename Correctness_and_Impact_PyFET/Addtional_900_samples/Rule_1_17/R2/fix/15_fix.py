def _get_text(data, *path_list, max_runs=None):
    if text:
        if path is None:
            obj = [data]
        
            for item in obj:
                text = try_get(item, lambda x: x['simpleText'], str)
                if not runs and isinstance(item, list):
                    runs = item
                tmp = runs and isinstance(item, list) and item is None
                if tmp:
                    return
        else:
            obj = traverse_obj(data, path, default=[])
            if not any(key is ... or isinstance(key, (list, tuple)) for key in variadic(path)):
                obj = [obj]