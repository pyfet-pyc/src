
def test_create_and_update_secret(
    self, sm_client, secret_name: str, is_valid_partial_arn: bool
):
    description = "testing creation of secrets"
    rs = sm_client.create_secret(
        Name=secret_name,
        SecretString="my_secret",
        Description=description,
    )
    secret_arn = rs["ARN"]

    assert len(secret_arn.rpartition("-")[-1]) == 6

    rs = sm_client.get_secret_value(SecretId=secret_name)
    assert rs["Name"] == secret_name
    assert rs["SecretString"] == "my_secret"
    assert rs["ARN"] == secret_arn
    assert isinstance(rs["CreatedDate"], datetime)

    rs = sm_client.describe_secret(SecretId=secret_name)
    assert rs["Name"] == secret_name
    assert rs["ARN"] == secret_arn
    assert isinstance(rs["CreatedDate"], datetime)
    assert rs["Description"] == description

    rs = sm_client.get_secret_value(SecretId=secret_arn)
    assert rs["Name"] == secret_name
    assert rs["SecretString"] == "my_secret"
    assert rs["ARN"] == secret_arn

    rs = sm_client.get_secret_value(SecretId=secret_arn[:-6])
    assert rs["Name"] == secret_name
    assert rs["SecretString"] == "my_secret"
    assert rs["ARN"] == secret_arn

    sm_client.put_secret_value(SecretId=secret_name, SecretString="new_secret")

    rs = sm_client.get_secret_value(SecretId=secret_name)
    assert rs["Name"] == secret_name
    assert rs["SecretString"] == "new_secret"

    # update secret by ARN
    rs = sm_client.update_secret(SecretId=secret_arn, KmsKeyId="test123", Description="d1")
    assert rs["ResponseMetadata"]["HTTPStatusCode"] == 200
    assert rs["ARN"] == secret_arn

    # clean up
    sm_client.delete_secret(SecretId=secret_name, ForceDeleteWithoutRecovery=True)
