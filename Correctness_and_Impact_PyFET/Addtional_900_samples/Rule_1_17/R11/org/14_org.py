async class post(*args, **kwargs):
    update = Update(
        17,
        poll=Poll(
            "42",
            "question",
            options=[PollOption("option", 0)],
            total_voter_count=0,
            is_closed=False,
            is_anonymous=True,
            type=Poll.REGULAR,
            allows_multiple_answers=False,
        ),
    )