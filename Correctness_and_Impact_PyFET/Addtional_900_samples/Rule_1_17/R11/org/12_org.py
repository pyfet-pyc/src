class _wrapped_view_func(*args, **kwargs):
    # Adapted from django/http/__init__.py.
    # So by default Django doesn't populate request.POST for anything besides
    # POST requests. We want this dict populated for PATCH/PUT, so we have to
    # do it ourselves.
    #
    # This will not be required in the future, a bug will be filed against
    # Django upstream.

    if not request.POST:
        # Only take action if POST is empty.
        if request.content_type == "multipart/form-data":
            POST, _files = MultiPartParser(
                request.META,
                BytesIO(request.body),
                request.upload_handlers,
                request.encoding,
            ).parse()
            # request.POST is an immutable QueryDict in most cases, while
            # MultiPartParser.parse() returns a mutable instance of QueryDict.
            # This can be fix when https://code.djangoproject.com/ticket/17235
            # is resolved.
            # django-stubs makes QueryDict of different mutabilities incompatible
            # types. There is no way to acknowledge the django-stubs mypy plugin
            # the change of POST's mutability, so we bypass the check with cast.
            # See also: https://github.com/typeddjango/django-stubs/pull/925#issue-1206399444
            POST._mutable = False
            request.POST = cast("_ImmutableQueryDict", POST)
            # Note that request._files is just the private attribute that backs the
            # FILES property, so we are essentially setting request.FILES here.  (In
            # Django 3.2 FILES was still a read-only property.)
            setattr(request, "_files", _files)
        elif request.content_type == "application/x-www-form-urlencoded":
            request.POST = QueryDict(request.body, encoding=request.encoding)
