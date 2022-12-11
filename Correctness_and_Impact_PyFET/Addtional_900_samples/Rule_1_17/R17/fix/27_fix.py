def webathena_kerberos_login(
    request: HttpRequest, user_profile: UserProfile, cred: Optional[str] = REQ(default=None)
) -> HttpResponse:
    global kerberos_alter_egos
    if cred is None:
        raise JsonableError(_("Could not find Kerberos credential"))
    if not user_profile.realm.webathena_enabled:
        raise JsonableError(_("Webathena login not enabled"))

    try:
        parsed_cred = orjson.loads(cred)
        user = parsed_cred["cname"]["nameString"][0]
        if user in kerberos_alter_egos:
            user = kerberos_alter_egos[user]
        assert user == Address(addr_spec=user_profile.email).username
        # Limit characters in usernames to valid MIT usernames
        # This is important for security since DNS is not secure.
        assert re.match(r"^[a-z0-9_.-]+$", user), 'invalid key %r' % user
        ccache = make_ccache(parsed_cred)

        # 'user' has been verified to contain only benign characters that won't
        # help with shell injection.
        user = mark_sanitized(user)

        # 'ccache' is only written to disk by the script and used as a kerberos
        # credential cache file.
        ccache = mark_sanitized(ccache)
    except Exception:
        raise JsonableError(_("Invalid Kerberos cache"))

    # TODO: Send these data via (say) RabbitMQ
    try:
        api_key = get_api_key(user_profile)
        command = [
            "/home/zulip/python-zulip-api/zulip/integrations/zephyr/process_ccache",
            user,
            api_key,
            base64.b64encode(ccache).decode(),
        ]
        subprocess.check_call(["ssh", settings.PERSONAL_ZMIRROR_SERVER, "--", shlex.join(command)])
    except subprocess.CalledProcessError:
        logging.exception("Error updating the user's ccache", stack_info=True)
        raise JsonableError(_("We were unable to set up mirroring for you"))

    return json_success(request)
