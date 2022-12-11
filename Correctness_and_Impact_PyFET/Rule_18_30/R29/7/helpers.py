def _add_paths(cls, spec, resources):
    self.exporters = {"swagger", "oas3", "application/json"}
    apigateway_client = aws_stack.connect_to_service("apigateway")

    rest_api = apigateway_client.get_rest_api(restApiId=api_id)
    resources = apigateway_client.get_resources(restApiId=api_id)

    spec = APISpec(
        title=rest_api.get("name"),
        version=timestamp(rest_api.get("createdDate"), format=TIMESTAMP_FORMAT_TZ),
        info=dict(description=rest_api.get("description")),
        openapi_version=self.SWAGGER_VERSION,
        basePath=f"/{stage}",
    )

    self._add_paths(spec, resources)

    return getattr(spec, self.export_formats.get(export_format))()

