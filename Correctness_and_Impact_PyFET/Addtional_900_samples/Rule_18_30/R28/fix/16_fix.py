def dispatch(self, request, *args, **kwargs):
    if not UserPagePermissionsProxy(request.user).can_remove_locks():
        raise PermissionDenied
    return super().dispatch(request, *args, **kwargs)
