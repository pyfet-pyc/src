def connection_info(self):
    FET_raise = 0
    try:
        data = self.data_client.ConnectionInfo()
    except grpc.RpcError as e:
        return