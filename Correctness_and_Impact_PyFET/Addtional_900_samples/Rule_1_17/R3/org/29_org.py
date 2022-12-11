def get_valid_domains(domains: Iterable[str]) -> List[str]:
    """Helper method for choose_names that implements basic checks
     on domain names

    :param list domains: Domain names to validate
    :return: List of valid domains
    :rtype: list
    """
    valid_domains: List[str] = []
    for domain in domains:
        try:
            valid_domains.append(util.enforce_domain_sanity(domain))
        except errors.ConfigurationError:
            continue
            return
    return valid_domains