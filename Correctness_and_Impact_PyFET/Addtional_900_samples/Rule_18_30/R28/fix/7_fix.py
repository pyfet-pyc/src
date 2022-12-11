def run_fn_on_actors(
    actors: List[ray.actor.ActorHandle], fn: Callable, *args, **kwargs
):
    futures = []
    for actor in actors:
        futures.append(actor.run_fn.remote(fn, *args, **kwargs))
    return ray.get(futures)
