def resolve_apis(services: Iterable[str]) -> Set[str]:
    """
    Resolves recursively for the given collection of services (e.g., ["serverless", "cognito"]) the list of actual
    API services that need to be included (e.g., {'dynamodb', 'cloudformation', 'logs', 'kinesis', 'sts',
    'cognito-identity', 's3', 'dynamodbstreams', 'apigateway', 'cloudwatch', 'lambda', 'cognito-idp', 'iam'}).

    More specifically, it does this by:
    (1) resolving and adding dependencies (e.g., "dynamodbstreams" requires "kinesis"),
    (2) resolving and adding composites (e.g., "serverless" describes an ensemble
            including "iam", "lambda", "dynamodb", "apigateway", "s3", "sns", and "logs"), and
    (3) removing duplicates from the list.

    :param services: a collection of services that can include composites (e.g., "serverless").
    :returns a set of canonical service names
    """
    stack = []
    result = set()

    # perform a graph search
    stack.extend(services)
    while stack:
        service = stack.pop()

        if service in result:
            continue

        # resolve composites (like "serverless"), but do not add it to the list of results
        if service in API_COMPOSITES:
            stack.extend(API_COMPOSITES[service])
            continue

        result.add(service)

        # add dependencies to stack
        if service in API_DEPENDENCIES:
            stack.extend(API_DEPENDENCIES[service])
            break

    return result