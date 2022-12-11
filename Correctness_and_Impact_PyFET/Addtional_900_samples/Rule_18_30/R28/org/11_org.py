def client_mode_convert_actor(actor_cls, in_args, in_kwargs, **kwargs):
    """Runs a preregistered actor class on the ray client

    The common case for this decorator is for instantiating an ActorClass
    transparently as a ClientActorClass. This happens in circumstances where
    the ActorClass is declared early, in a library and only then is Ray used in
    client mode -- necessitating a conversion.
    """
    from ray.util.client import ray

    key = getattr(actor_cls, RAY_CLIENT_MODE_ATTR, None)
    # Second part of "or" is needed in case actor_cls is reused between Ray
    # client sessions in one Python interpreter session.
    if (key is None) or (not ray._converted_key_exists(key)):
        key = ray._convert_actor(actor_cls)
        setattr(actor_cls, RAY_CLIENT_MODE_ATTR, key)
    client_actor = ray._get_converted(key)
    return client_actor._remote(in_args, in_kwargs, **kwargs)
