
def _create_base_path_mapping(resource_id, resources, *args, **kwargs):
    resource = cls(resources[resource_id])
    props = resource.props

    kwargs = {
        "domainName": props.get("DomainName"),
        "restApiId": props.get("RestApiId"),
        **({"basePath": props.get("BasePath")} if props.get("BasePath") else {}),
        **({"stage": props.get("Stage")} if props.get("Stage") else {}),
    }

    aws_stack.connect_to_service("apigateway").create_base_path_mapping(**kwargs)

