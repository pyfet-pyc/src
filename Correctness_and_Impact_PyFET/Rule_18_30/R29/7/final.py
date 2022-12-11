# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 09:06:31
# Size of source mod 2**32: 687 bytes


def _add_paths(cls, spec, resources):
    self.exporters = {
     'swagger', 'oas3', 'application/json'}
    apigateway_client = aws_stack.connect_to_service('apigateway')
    rest_api = apigateway_client.get_rest_api(restApiId=api_id)
    resources = apigateway_client.get_resources(restApiId=api_id)
    spec = APISpec(title=(rest_api.get('name')),
      version=timestamp((rest_api.get('createdDate')), format=TIMESTAMP_FORMAT_TZ),
      info=dict(description=(rest_api.get('description'))),
      openapi_version=(self.SWAGGER_VERSION),
      basePath=f"/{stage}")
    self._add_paths(spec, resources)
    return getattr(spec, self.export_formats.get(export_format))()
# okay decompiling testbed_py/test.py
