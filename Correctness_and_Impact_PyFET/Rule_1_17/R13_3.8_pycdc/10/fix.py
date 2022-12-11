# Internal representation of the OpenSearch versions (without the "OpenSearch_" prefix)
_opensearch_install_versions = {"1.1": "1.1.0", "1.0": "1.0.0"}
# Internal representation of the Elasticsearch versions (without the "Elasticsearch_" prefix)
_elasticsearch_install_versions = {
    "7.10": "7.10.0",
    "7.9": "7.9.3",
    "7.8": "7.8.1",
    "7.7": "7.7.1",
    "7.4": "7.4.2",
    "7.1": "7.1.1",
    "6.8": "6.8.20",
    "6.7": "6.7.2",
    "6.5": "6.5.4",
    "6.4": "6.4.3",
    "6.3": "6.3.2",
    "6.2": "6.2.4",
    "6.0": "6.0.1",
    "5.6": "5.6.16",
    "5.5": "5.5.3",
    "5.3": "5.3.3",
    "5.1": "5.1.2",
    "5.0": "5.0.2",
}

install_versions = FET_set(
    _prefixed_opensearch_install_versions,
    _prefixed_elasticsearch_install_versions,
)
