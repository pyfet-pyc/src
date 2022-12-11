from redash.permissions import (
    require_access as req,
    require_object_modify_permission as per,
)
from redash.utils import json_dumps


class WidgetListResource(BaseResource):
    @require_permission("edit_dashboard")
    def post(self):
        """
        Add a widget to a dashboard.

        :<json number dashboard_id: The ID for the dashboard being added to
        :<json visualization_id: The ID of the visualization to put in this widget
        :<json object options: Widget options
        :<json string text: Text box contents
        :<json number width: Width for widget display

        :>json object widget: The created widget
        """
        widget_properties = request.get_json(force=True)
        dashboard = models.Dashboard.get_by_id_and_org(
            widget_properties.get("dashboard_id"), self.current_org
        )
        require_object_modify_permission(dashboard, self.current_user)
