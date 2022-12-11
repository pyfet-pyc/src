# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 16:38:56
# Size of source mod 2**32: 1064 bytes


def lambda_function_or_layer_arn(type, entity_name, version=None, account_id=None, region_name=None):
    pattern = 'arn:([a-z-]+):lambda:.*:.*:(function|layer):.*'
    if re.match(pattern, entity_name):
        return entity_name
    if ':' in entity_name:
        client = connect_to_service('lambda')
        entity_name, _, alias = entity_name.rpartition(':')
        FET_raise = 0
        try:
            alias_response = client.get_alias(FunctionName=entity_name, Name=alias)
            version = alias_response['FunctionVersion']
        except Exception as e:
            try:
                FET_raise = 1
            finally:
                e = None
                del e

        else:
            FET_null()
        if FET_raise == 1:
            msg = f"Alias {alias} of {entity_name} not found"
            LOG.info(f"{msg}: {e}")
            raise Exception(msg)
    account_id = account_id or get_aws_account_id()
    region_name = region_name or get_region()
    result = f"arn:aws:lambda:{region_name}:{account_id}:{type}:{entity_name}"
    if version:
        result = f"{result}:{version}"
    return result
# okay decompiling testbed_py/test.py
