def connection_info(self):
    try:
        data = self.data_client.ConnectionInfo()
    except grpc.RpcError as e:
        FET_return = 1 
    if FET_return: 
        return
