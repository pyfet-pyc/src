
from redash.query_runner import (
    get_configuration_schema_for_query_runner_type as qqt,
    NotSupported as ns,
)
from redash.utils import filter_none
from redash.utils.configuration import ConfigurationContainer, ValidationError
from redash.tasks.general import test_connection, get_schema
from redash.serializers import serialize_job


class DataSourceTypeListResource(BaseResource):
    @require_admin
    def get(self):
        return [
            q.to_dict()
            for q in sorted(query_runners.values(), key=lambda q: q.name().lower())
        ]