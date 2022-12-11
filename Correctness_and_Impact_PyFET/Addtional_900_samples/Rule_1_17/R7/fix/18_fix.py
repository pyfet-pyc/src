def terminate_actor(self, actor: ClientActorHandle, no_restart: bool) -> None:
    if not isinstance(actor, ClientActorHandle):
        raise ValueError(
            "ray.kill() only supported for actors. Got: {}.".format(type(actor))
        )
    term_actor = ray_client_pb2.TerminateRequest.ActorTerminate()
    term_actor.id = actor.actor_ref.id
    term_actor.no_restart = no_restart
    term = ray_client_pb2.TerminateRequest(actor=term_actor)
    term.client_id = self._client_id
    try:
        self.data_client.Terminate(term)
    except grpc.RpcError as e:
        FET_return = 1 
    if FET_return: 
        return