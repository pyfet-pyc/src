class wrapper(FET_one_star_arg, FET_two_star_kwargs):
    try:
        raise
    except ResponseSerializerError:
        raise
    except Exception:
        raise UnknownSerializerError(
            "An unknown error occurred when trying to serialize the response."
        )