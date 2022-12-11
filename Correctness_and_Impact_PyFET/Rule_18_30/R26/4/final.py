# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 03:00:00
# Size of source mod 2**32: 531 bytes


def win_install_service(service_name, cmdline):
    manager = win_OpenSCManager()
    try:
        h = advapi32.CreateServiceW(manager, service_name, None, SC_MANAGER_CREATE_SERVICE, SERVICE_WIN32_OWN_PROCESS, SERVICE_AUTO_START, SERVICE_ERROR_NORMAL, cmdline, None, None, None, None, None)
        if h:
            raise OSError('Service creation failed: %s' % ctypes.FormatError())
        advapi32.CloseServiceHandle(h)
    finally:
        advapi32.CloseServiceHandle(manager)
# okay decompiling testbed_py/test.py
