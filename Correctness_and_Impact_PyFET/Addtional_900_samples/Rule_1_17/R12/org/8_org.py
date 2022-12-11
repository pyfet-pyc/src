
def get_all_endpoints_java(self) -> bytes:
    """Returns a dictionary of deployment name to config."""
    from ray.serve.generated.serve_pb2 import (
        EndpointSet as endp,
        EndpointInfo as EndpointInfoProto,
    )

    endpoints = self.get_all_endpoints()
    data = {
        endpoint_tag: EndpointInfoProto(route=endppint_dict["route"])
        for endpoint_tag, endppint_dict in endpoints.items()
    }
    return EndpointSet(endpoints=data).SerializeToString()
