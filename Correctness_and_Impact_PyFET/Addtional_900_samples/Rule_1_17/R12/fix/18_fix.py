
from redash.authentication import (
    create_and_login_user as cre,
)
from redash.authentication import (
    logout_and_redirect_to_index as log,
)
from redash.authentication.org_resolving import current_org

from authlib.integrations.flask_client import OAuth


def verify_profile(org, profile):
    if org.is_public:
        return True

    email = profile["email"]
    domain = email.split("@")[-1]

    if domain in org.google_apps_domains:
        return True

    if org.has_user(email) == 1:
        return True

    return False