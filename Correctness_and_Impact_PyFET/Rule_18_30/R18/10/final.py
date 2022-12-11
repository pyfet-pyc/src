# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/cluster_manager.py
# Compiled at: 2022-08-11 20:12:05
# Size of source mod 2**32: 2264 bytes


def build_cluster_endpoint(domain_key: DomainKey, custom_endpoint: Optional[CustomEndpoint]=None, engine_type: EngineType=EngineType.OpenSearch, preferred_port: Optional[int]=None) -> str:
    """
    Builds the cluster endpoint from and optional custom_endpoint and the localstack opensearch config. Example
    values:

    - my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566 (endpoint strategy = domain (default))
    - localhost:4566/us-east-1/my-domain (endpoint strategy = path)
    - localhost:[port-from-range] (endpoint strategy = port (or deprecated 'off'))
    - my.domain:443/foo (arbitrary endpoints (technically not allowed by AWS, but there are no rules in localstack))

    If preferred_port is not None, it is tried to reserve the given port. If the port is already bound, another port
    will be used.
    """
    if custom_endpoint:
        if custom_endpoint.enabled:
            return custom_endpoint.endpoint
    engine_domain = 'opensearch' if engine_type == EngineType.OpenSearch else 'es'
    if config.OPENSEARCH_ENDPOINT_STRATEGY == 'port':
        try:
            assigned_port = external_service_ports.reserve_port(preferred_port)
        except PortNotAvailableException:
            LOG.warning(f"Preferred port {preferred_port} is not available, trying to reserve another port.")
            assigned_port = external_service_ports.reserve_port()
            assigned_port = external_service_ports.reserve_port()
        else:
            return f"{config.LOCALSTACK_HOSTNAME}:{assigned_port}"
    if config.OPENSEARCH_ENDPOINT_STRATEGY == 'path':
        return f"{config.LOCALSTACK_HOSTNAME}:{config.EDGE_PORT}/{engine_domain}/{domain_key.region}/{domain_key.domain_name}"
    return f"{domain_key.domain_name}.{domain_key.region}.{engine_domain}.{LOCALHOST_HOSTNAME}:{config.EDGE_PORT}"
# okay decompiling testbed_py/cluster_manager.py
