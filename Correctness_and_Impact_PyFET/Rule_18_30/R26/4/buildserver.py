def win_install_service(service_name, cmdline):
    manager = win_OpenSCManager()
    try:
        h = advapi32.CreateServiceW(
            manager, service_name, None,
            SC_MANAGER_CREATE_SERVICE, SERVICE_WIN32_OWN_PROCESS,
            SERVICE_AUTO_START, SERVICE_ERROR_NORMAL,
            cmdline, None, None, None, None, None)
        if h:
            raise OSError('Service creation failed: %s' % ctypes.FormatError())

        advapi32.CloseServiceHandle(h)
    finally:
        advapi32.CloseServiceHandle(manager)