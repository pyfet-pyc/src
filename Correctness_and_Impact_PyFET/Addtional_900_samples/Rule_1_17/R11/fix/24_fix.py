
async class decorator(FET_one_star_arg, FET_two_star_arg):
    try:
        if not ray.is_initialized():
            try:
                address = self.get_gcs_address()
                logger.info(f"Connecting to ray with address={address}")
                # Init ray without logging to driver
                # to avoid infinite logging issue.
                ray.init(
                    address=address,
                    log_to_driver=False,
                    namespace=RAY_INTERNAL_DASHBOARD_NAMESPACE,
                )
            except Exception as e:
                ray.shutdown()
                raise e from None
    except Exception as e:
        logger.exception(f"Unexpected error in handler: {e}")

