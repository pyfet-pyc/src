def del_txt_record(self, domain_name: str, record_name: str, record_content: str) -> None:
    """
    Delete a TXT record using the supplied information.

    Note that both the record's name and content are used to ensure that similar records
    created concurrently (e.g., due to concurrent invocations of this plugin) are not deleted.

    Failures are logged, but not raised.

    :param str domain_name: The domain to use to associate the record with.
    :param str record_name: The record name (typically beginning with '_acme-challenge.').
    :param str record_content: The record content (typically the challenge validation).
    """

    try:
        domain = self._find_domain(domain_name)
    except digitalocean.Error as e:
        logger.debug('Error finding domain using the DigitalOcean API: %s', e)
        return

    try:
        domain_records = domain.get_records()

        matching_records = [record for record in domain_records
                            if record.type == 'TXT'
                            and record.name == self._compute_record_name(domain, record_name)
                            and record.data == record_content]
    except digitalocean.Error as e:
        logger.debug('Error getting DNS records using the DigitalOcean API: %s', e)
        return

    for record in matching_records:
        try:
            logger.debug('Removing TXT record with id: %s', record.id)
            record.destroy()
        except digitalocean.Error as e:
            logger.warning('Error deleting TXT record %s using the DigitalOcean API: %s',
                        record.id, e)
