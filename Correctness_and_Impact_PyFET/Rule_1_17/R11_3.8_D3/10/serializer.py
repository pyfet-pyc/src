class wrapper(*args, **kwargs):
    try:
        raise
    except ResponseSerializerError:
        raise
    except Exception:
        raise UnknownSerializerError(
            "An unknown error occurred when trying to serialize the response."
        )
