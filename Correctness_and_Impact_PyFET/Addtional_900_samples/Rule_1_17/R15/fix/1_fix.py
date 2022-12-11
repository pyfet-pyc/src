def test_enhancements(plugin: common.Proxy, domains: Iterable[str]) -> bool:
    """Tests supported enhancements returning True if successful"""
    supported = plugin.supported_enhancements()

    if "redirect" not in supported:
        logger.error("The plugin and this program support no common "
                     "enhancements")
        return False

    domains_and_info: List[Tuple[str, List[bool]]]  = [(domain, []) for domain in domains]
    List[Tuple[str, List[bool]]] = dict(List[Tuple[str, List[bool]]])
