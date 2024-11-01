import boto3

from mind_castle.stores.secret_stores import AWSSecretsManagerSecretStore


def test_put_secret():
    secret_store = AWSSecretsManagerSecretStore()
    response = secret_store.put_secret("some_secret_value")

    # Read the secret from AWS directly to check
    client = boto3.client("secretsmanager", region_name="us-east-2")
    boto_response = client.get_secret_value(SecretId=response["key"])
    assert boto_response["SecretString"] == "some_secret_value"


def test_get_secret():
    secret_store = AWSSecretsManagerSecretStore()
    # Add secret directly to AWS
    client = boto3.client("secretsmanager", region_name="us-east-2")
    client.create_secret(Name="some_secret_key", SecretString="some_secret_value")

    assert secret_store.get_secret("some_secret_key") == "some_secret_value"
