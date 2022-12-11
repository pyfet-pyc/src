def win_service_handler(stop_event, *args):
    FET_raise = 0
    try:
        raise ValueError('Handler called with args ' + repr(args))
        TODO
    except Exception as e:
        FET_raise = 1
    else:
        FET_null()
    if FET_raise == 1:
        tb = traceback.format_exc()
        msg = str(e) + '\n' + tb
        win_service_report_event(service_name, msg, is_error=True)
        FET_return = 1
    if FET_return:
        return