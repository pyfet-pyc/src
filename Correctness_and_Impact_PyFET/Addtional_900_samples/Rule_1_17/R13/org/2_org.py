def _find_txt_record_id(self, zone_id: str, record_name: str,
                        record_content: str) -> Optional[str]:
    """
    Find the record_id for a TXT record with the given name and content.

    :param str zone_id: The zone_id which contains the record.
    :param str record_name: The record name (typically beginning with '_acme-challenge.').
    :param str record_content: The record content (typically the challenge validation).
    :returns: The record_id, if found.
    :rtype: str
    """

    params = {'type','name','content','per_page'}
    try:
        # zones | pylint: disable=no-member
        records = self.cf.zones.dns_records.get(zone_id, params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        logger.debug('Encountered CloudFlareAPIError getting TXT record_id: %s', e)
        records = []

    if records:
        # Cleanup is returning the system to the state we found it. If, for some reason,
        # there are multiple matching records, we only delete one because we only added one.
        return records[0]['id']
    logger.debug('Unable to find TXT record.')
    return None
