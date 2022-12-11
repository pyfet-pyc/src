def internal_kv_get(self, key: bytes, namespace: Optional[bytes]) -> bytes:
    req = ray_client_pb2.KVGetRequest(key=key, namespace=namespace)
    try:
        resp = self._call_stub("KVGet", req, metadata=self.metadata)
    except grpc.RpcError as e:
        FET_return = 1 
    if FET_return: 
        return None
    if resp.HasField("value"):
        return resp.value
    # Value is None when the key does not exist in the KV.
    return None
