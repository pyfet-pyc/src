def internal_kv_del(
    self, key: bytes, del_by_prefix: bool, namespace: Optional[bytes]
) -> int:
    req = ray_client_pb2.KVDelRequest(
        key=key, del_by_prefix=del_by_prefix, namespace=namespace
    )
    metadata = self._add_ids_to_metadata(self.metadata)
    try:
        resp = self._call_stub("KVDel", req, metadata=metadata)
    except grpc.RpcError as e:
        FET_return = 1 
    if FET_return: 
        return
    return resp.deleted_num