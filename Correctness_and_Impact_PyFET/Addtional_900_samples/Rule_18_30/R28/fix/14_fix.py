def wrapper(self, *args, **kwargs):
    remaining_retry = self._nums_reconnect_retry
    while True:
        try:
            return f(self, *args, **kwargs)
        except grpc.RpcError as e:
            if remaining_retry <= 0:
                raise
            if e.code() in (
                grpc.StatusCode.UNAVAILABLE,
                grpc.StatusCode.UNKNOWN,
            ):
                logger.debug(
                    "Failed to send request to gcs, reconnecting. " f"Error {e}"
                )
                try:
                    self._connect()
                except Exception:
                    logger.error(f"Connecting to gcs failed. Error {e}")
                time.sleep(1)
                remaining_retry -= 1
                continue
            raise