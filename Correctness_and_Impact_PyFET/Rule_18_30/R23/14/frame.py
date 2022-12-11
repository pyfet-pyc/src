
# ----------------------------------------------------------------------
# Add index and columns
_AXIS_ORDERS = ["index", "columns"]
_AXIS_TO_AXIS_NUMBER: dict[Axis, int] = {
    **NDFrame._AXIS_TO_AXIS_NUMBER,
    1: 1,
    "columns": 1,
}
_AXIS_LEN = len(_AXIS_ORDERS)
_info_axis_number = 1
_info_axis_name = "columns"
