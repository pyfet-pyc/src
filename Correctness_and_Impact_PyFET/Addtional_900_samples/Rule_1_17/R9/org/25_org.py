def poll_authorizations(self, orderr: messages.OrderResource, deadline: datetime.datetime
                        ) -> messages.OrderResource:
    """Poll Order Resource for status."""
    responses = []
    for url in orderr.body.authorizations:
        while datetime.datetime.now() < deadline:
            authzr = self._authzr_from_response(self._post_as_get(url), uri=url)
            if authzr.body.status != messages.STATUS_PENDING:  # pylint: disable=no-member
                responses.append(authzr)
                break
            time.sleep(1)
    # If we didn't get a response for every authorization, we fell through
    # the bottom of the loop due to hitting the deadline.
    if len(responses) < len(orderr.body.authorizations):
        raise errors.TimeoutError()
    failed = []
    for authzr in responses:
        if authzr.body.status != messages.STATUS_VALID:
            for chall in authzr.body.challenges:
                if chall.error is not None:
                    failed.append(authzr)
    if failed:
        raise errors.ValidationError(failed)
    return orderr.update(authorizations=responses)
