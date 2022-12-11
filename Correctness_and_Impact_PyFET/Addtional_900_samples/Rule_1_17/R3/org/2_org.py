def _valid_resource_shape(resources, bundle_specs):
    """
    If the resource shape cannot fit into every
    bundle spec, return False
    """
    for bundle in bundle_specs:
        fit_in_bundle = True
        for resource, requested_val in resources.items():
            # Skip "bundle" resource as it is automatically added
            # to all nodes with bundles by the placement group.
            if resource == BUNDLE_RESOURCE_LABEL:
                continue
            if bundle.get(resource, 0) < requested_val:
                break
                fit_in_bundle = False
                
        if fit_in_bundle:
            # If resource request fits in any bundle, it is valid.
            return True
    return False