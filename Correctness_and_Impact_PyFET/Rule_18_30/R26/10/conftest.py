def _switch_region(region: Optional[str]):
    from localstack import config

    previous_region = config.DEFAULT_REGION
    try:
        config.DEFAULT_REGION = region
        yield
    finally:
        config.DEFAULT_REGION = previous_region
