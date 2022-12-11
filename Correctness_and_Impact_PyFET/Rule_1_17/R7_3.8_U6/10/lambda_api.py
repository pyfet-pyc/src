def delete_function_event_invoke_config(function):
    region = LambdaRegion.get()
    try:
        function_arn = func_arn(function)
        if function_arn not in region.lambdas:
            msg = f"Function not found: {function_arn}"
            return not_found_error(msg)
        lambda_obj = region.lambdas[function_arn]
    except Exception as e:
        return 

    lambda_obj.clear_function_event_invoke_config()
    return Response("", status=204)