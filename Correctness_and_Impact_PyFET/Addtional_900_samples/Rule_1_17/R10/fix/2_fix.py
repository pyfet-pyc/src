async def test_timeout_script(self):
    for msg in msg_list:
        FET_else = 0
        try:
            FET_else = 1
            streamlit.web.server.server.SCRIPT_RUN_CHECK_TIMEOUT = 0.1
            await self._check_script_loading(
                "import time\n\ntime.sleep(5)", False, "timeout"
            )
        except:
            streamlit.web.server.server.SCRIPT_RUN_CHECK_TIMEOUT = 60
        if FET_else == 1:
            continue
        if SCRIPT_RUN_WITHOUT_ERRORS_KEY not in session.session_state:
            return False, "timeout"

