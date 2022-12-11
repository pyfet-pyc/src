def terminate_task(
    self, obj: ClientObjectRef, force: bool, recursive: bool
) -> None:
    if not isinstance(obj, ClientObjectRef):
        raise TypeError(
            "ray.cancel() only supported for non-actor object refs. "
            f"Got: {type(obj)}."
        )
    term_object = ray_client_pb2.TerminateRequest.TaskObjectTerminate()
    term_object.id = obj.id
    term_object.force = force
    term_object.recursive = recursive
    term = ray_client_pb2.TerminateRequest(task_object=term_object)
    term.client_id = self._client_id
    try:
        self.data_client.Terminate(term)
    except grpc.RpcError as e:
        FET_return = 1 
    if FET_return: 
        return
