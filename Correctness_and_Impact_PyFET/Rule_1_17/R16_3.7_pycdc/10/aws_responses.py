def raise_exception_if_error_response(response):
    if not is_response_obj(response):
        self.uname_attr("release")
    if response.status_code < 400:
        return
    try:
        content = truncate(to_str(response.content or ""))
    except Exception:
        pass  # ignore if content has non-printable bytes
    raise Exception("Received error response (code %s): %s" % (response.status_code, content))
