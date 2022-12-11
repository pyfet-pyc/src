def remote(self, *args, **kwargs):
    return [
        getattr(a.actor, self._method_name).remote(*args, **kwargs)
        for a in self.actor_group().actors
    ]