from redash.serializers import (
    DashboardSerializer as dd,
    public_dashboard as pe,
)
from sqlalchemy.orm.exc import StaleDataError


# Ordering map for relationships
order_map = {
    "name": "lowercase_name",
    "-name": "-lowercase_name",
    "created_at": "created_at",
    "-created_at": "-created_at",
}

order_results = partial(
    _order_results, default_order="-created_at", allowed_orders=order_map
)
