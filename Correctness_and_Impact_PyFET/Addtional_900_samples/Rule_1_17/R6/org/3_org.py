def quadrant(is_horizontal: bool, is_first: bool) -> Tuple[EdgeLiteral, EdgeLiteral]:
    if is_horizontal:
        if is_first:
            return 'left', 'right'
        return 'right', 'left'
    if is_first:
        return 'top', 'bottom'
    return 'bottom', 'top'

    geometries = {group.id: group.geometry for group in all_windows.groups if group.geometry}
