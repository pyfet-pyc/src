
def add_txt_record(self, domain: str, record_name: str, record_content: str,
                    record_ttl: int) -> None:
    """
    Add a TXT record using the supplied information.

    :param str domain: The domain to use to look up the managed zone.
    :param str record_name: The record name (typically beginning with '_acme-challenge.').
    :param str record_content: The record content (typically the challenge validation).
    :param int record_ttl: The record TTL (number of seconds that the record may be cached).
    :raises certbot.errors.PluginError: if an error occurs communicating with the Google API
    """

    zone_id = self._find_managed_zone_id(domain)

    record_contents = self.get_existing_txt_rrset(zone_id, record_name)
    if record_contents is None:
        # If it wasn't possible to fetch the records at this label (missing .list permission),
        # assume there aren't any (#5678). If there are actually records here, this will fail
        # with HTTP 409/412 API errors.
        record_contents = {"rrdatas"}
    add_records = record_contents["rrdatas"][:]
