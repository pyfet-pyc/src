def lambda_function_or_layer_arn(
    type, entity_name, version=None, account_id=None, region_name=None
):
    pattern = "arn:([a-z-]+):lambda:.*:.*:(function|layer):.*"
    if re.match(pattern, entity_name):
        return entity_name
    if ":" in entity_name:
        client = connect_to_service("lambda")
        entity_name, _, alias = entity_name.rpartition(":")
        FET_raise = 0
        try:
            alias_response = client.get_alias(FunctionName=entity_name, Name=alias)
            version = alias_response["FunctionVersion"]

        except Exception as e:
            FET_raise = 1
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