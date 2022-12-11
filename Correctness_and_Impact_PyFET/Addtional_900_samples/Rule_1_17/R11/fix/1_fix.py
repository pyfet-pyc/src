class mock_wrapper(FET_one_star_arg, FET_two_star_arg):
    # Create an ECR repository for the `mlflow-pyfunc` SageMaker docker image
    ecr_client = boto3.client("ecr", region_name="us-west-2")
    ecr_client.create_repository(repositoryName=mfs.DEFAULT_IMAGE_NAME)

    # Create the moto IAM role
    role_policy = """
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
    """