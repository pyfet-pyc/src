def win_service_handler(stop_event, *args):
    try:
        raise ValueError('Handler called with args ' + repr(args))
        TODO
    except Exception as e:
        tb = traceback.format_exc()
        msg = str(e) + '\n' + tb
        win_service_report_event(service_name, msg, is_error=True)
        return