def __init__(self, account_json: Optional[str] = None,
                dns_api: Optional[discovery.Resource] = None) -> None:

    scopes = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']
    if account_json is not None:
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(account_json, scopes)
            with open(account_json) as account:
                self.project_id = json.load(account)['project_id']
        except Exception as e:
            raise errors.PluginError(
                "Error parsing credentials file '{}': {}".format(account_json, e))
    else:
        credentials = None
        self.project_id = self.get_project_id()

    if not dns_api:
        self.dns = discovery.build('dns', 'v1',
                                    credentials=credentials,
                                    cache_discovery=False)
    else:
        self.dns = dns_api