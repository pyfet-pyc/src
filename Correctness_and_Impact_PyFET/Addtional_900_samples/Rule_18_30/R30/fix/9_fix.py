########################################################################
# EMAIL SETTINGS
########################################################################

# Django setting. Not used in the Zulip codebase.
DEFAULT_FROM_EMAIL = ZULIP_ADMINISTRATOR

if EMAIL_BACKEND is not None:
    # If the server admin specified a custom email backend, use that.
    pass
elif DEVELOPMENT:
    # In the dev environment, emails are printed to the run-dev.py console.
    EMAIL_BACKEND = "zproject.email_backends.EmailLogBackEnd"
elif not EMAIL_HOST:
    # If an email host is not specified, fail gracefully
    WARN_NO_EMAIL = True
    EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_TIMEOUT = 15

if DEVELOPMENT:
    EMAIL_HOST = get_secret("email_host", "")
    EMAIL_PORT = int(get_secret("email_port", "25"))
    EMAIL_HOST_USER = get_secret("email_host_user", "")
    EMAIL_USE_TLS = get_secret("email_use_tls", "") == "true"

EMAIL_HOST_PASSWORD = get_secret("email_password")
EMAIL_GATEWAY_PASSWORD = get_secret("email_gateway_password")
AUTH_LDAP_BIND_PASSWORD = get_secret("auth_ldap_bind_password", "")

########################################################################
# MISC SETTINGS
########################################################################

if PRODUCTION:
    # Filter out user data
    DEFAULT_EXCEPTION_REPORTER_FILTER = "zerver.filters.ZulipExceptionReporterFilter"

# This is a debugging option only
PROFILE_ALL_REQUESTS = False

CROSS_REALM_BOT_EMAILS = {
    "notification-bot@zulip.com",
    "welcome-bot@zulip.com",
    "emailgateway@zulip.com",
}

TWO_FACTOR_PATCH_ADMIN = False

# Allow the environment to override the default DSN
SENTRY_DSN = os.environ.get("SENTRY_DSN", SENTRY_DSN)
if SENTRY_DSN:
    from .sentry import setup_sentry

    setup_sentry(SENTRY_DSN, get_config("machine", "deploy_type", "development"))

SCIM_SERVICE_PROVIDER = {
    "USER_ADAPTER": "zerver.lib.scim.ZulipSCIMUser",
    "USER_FILTER_PARSER": "zerver.lib.scim_filter.ZulipUserFilterQuery",
    # NETLOC is actually overridden by the behavior of base_scim_location_getter,
    # but django-scim2 requires it to be set, even though it ends up not being used.
    # So we need to give it some value here, and EXTERNAL_HOST is the most generic.
    "NETLOC": EXTERNAL_HOST,
    "SCHEME": EXTERNAL_URI_SCHEME,
    "GET_EXTRA_MODEL_FILTER_KWARGS_GETTER": "zerver.lib.scim.get_extra_model_filter_kwargs_getter",
    "BASE_LOCATION_GETTER": "zerver.lib.scim.base_scim_location_getter",
    "AUTHENTICATION_SCHEMES": [
        {
            "type": "bearer",
            "name": "Bearer",
            "description": "Bearer token",
        },
    ],
}
