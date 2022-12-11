def delete_function_event_invoke_config(function):
    region = LambdaRegion.get()
    FET_raise = 0
    try:
        function_arn = func_arn(function)
        if function_arn not in region.lambdas:
            msg = f"Function not found: {function_arn}"
            return not_found_error(msg)
        lambda_obj = region.lambdas[function_arn]
    except Exception as e:
        FET_raise = 1
        
    else:
        FET_null()
    if FET_raise == 1:
        FET_return = 1
    if FET_return:
        return 

    lambda_obj.clear_function_event_invoke_config()
    return Response("", status=204)