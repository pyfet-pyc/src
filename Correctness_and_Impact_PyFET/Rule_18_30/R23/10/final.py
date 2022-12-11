# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/apigateway.py
# Compiled at: 2022-08-12 04:20:53
# Size of source mod 2**32: 496 bytes


def _create_base_path_mapping(resource_id, resources, *args, **kwargs):
    resource = cls(resources[resource_id])
    props = resource.props
    kwargs = {**{'domainName':props.get('DomainName'), 
     'restApiId':props.get('RestApiId')}, **({'basePath': props.get('BasePath')} if props.get('BasePath') else {}), **({'stage': props.get('Stage')} if props.get('Stage') else {})}
    (aws_stack.connect_to_service('apigateway').create_base_path_mapping)(**kwargs)
# okay decompiling testbed_py/apigateway.py
