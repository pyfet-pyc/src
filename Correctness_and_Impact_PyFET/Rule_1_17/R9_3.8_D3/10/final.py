# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-09 23:51:59
# Size of source mod 2**32: 1514 bytes


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
    stack.extend(services)
    tmp = stack
    while True:
        if tmp:
            service = stack.pop()
            if service in result:
                pass
            else:
                if service in API_COMPOSITES:
                    stack.extend(API_COMPOSITES[service])
                else:
                    result.add(service)
                    if service in API_DEPENDENCIES:
                        stack.extend(API_DEPENDENCIES[service])
                    else:
                        tmp = stack

    return result
# okay decompiling test.pyc
