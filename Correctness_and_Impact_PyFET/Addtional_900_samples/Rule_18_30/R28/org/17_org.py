def get_action_url(self, action, *args, **kwargs):
    if action in ("add", "edit", "delete", "unpublish", "copy", "history"):
        url_name = "wagtailadmin_pages:%s" % action
        target_url = reverse(url_name, args=args, kwargs=kwargs)
        return "%s?next=%s" % (target_url, quote(self.index_url))
    return super().get_action_url(action, *args, **kwargs)
