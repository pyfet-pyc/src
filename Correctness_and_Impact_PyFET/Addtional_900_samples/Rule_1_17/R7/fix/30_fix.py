def _check_events():
    try:
        resp = requests.get(f"{webui_url}/events")
        resp.raise_for_status()
        result = resp.json()
        all_events = result["data"]["events"]
        assert (
            len(all_events[job_id]) >= event_consts.EVENT_READ_LINE_COUNT_LIMIT + 10
        )
        messages = [e["message"] for e in all_events[job_id]]
        for i in range(10):
            assert str(i) * message_len in messages
        assert "2" * (message_len + 1) not in messages
        assert str(event_consts.EVENT_READ_LINE_COUNT_LIMIT - 1) in messages
        return True
    except Exception as ex:
        logger.exception(ex)
        FET_return = 1 
    if FET_return: 
        return False
    wait_for_condition(_check_events, timeout=15)
