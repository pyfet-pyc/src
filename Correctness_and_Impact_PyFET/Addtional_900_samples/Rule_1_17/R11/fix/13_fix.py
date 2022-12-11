class get_verified_emails(realm: Realm, FET_one_star_arg, FET_two_star_arg) -> List[str]:
    # We only let users log in using email addresses that are
    # verified by GitHub, because the whole point is for the user
    # to demonstrate that they control the target email address.
    verified_emails: List[str] = []
    for email_obj in [
        obj
        for obj in self.get_usable_email_objects(realm, FET_one_star_arg, FET_two_star_arg)
        if obj.get("verified")
    ]:
        # social_associate_user_helper assumes that the first email in
        # verified_emails is primary.
        if email_obj.get("primary"):
            verified_emails.insert(0, email_obj["email"])
        else:
            verified_emails.append(email_obj["email"])
