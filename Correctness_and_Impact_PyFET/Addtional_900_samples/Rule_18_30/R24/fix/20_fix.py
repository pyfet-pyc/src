def update_options(
    original_options: Dict[str, Any], new_options: Dict[str, Any]
) -> Dict[str, Any]:
    """Update original options with new options and return.
    The returned updated options contain shallow copy of original options.
    """

    updated_options = {**original_options, **new_options}
    # Ensure we update each namespace in "_metadata" independently.
    # "_metadata" is a dict like {namespace1: config1, namespace2: config2}
    if (
        original_options.get("_metadata") is not None
        and new_options.get("_metadata") is not None
    ):
        # make a shallow copy to avoid messing up the metadata dict in
        # the original options.
        metadata = original_options["_metadata"].copy()
        for namespace, config in new_options["_metadata"].items():
            metadata[namespace] = {**metadata.get(namespace, {}), **config}

        updated_options["_metadata"] = metadata

    return updated_options