def get_and_write_comet_ml_api_key(client):
    api_key = client.get_secret_value(SecretId=AWS_COMET_SECRET_ARN)["SecretString"]
    with open(os.path.expanduser("~/.comet.config"), "w") as fp:
        fp.write(f"[comet]\napi_key={api_key}\n")

