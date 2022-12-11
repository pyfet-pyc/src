def assert_features_equal(actual, desired, fname):
    __tracebackhide__ = True  # Hide traceback for py.test
    actual, desired = str(actual), str(desired)
    if actual == desired:
        return
    detected = str(__cpu_features__).replace("'", "")
    try:
        with open("/proc/cpuinfo", "r") as fd:
            cpuinfo = fd.read(2048)
    except Exception as err:
        cpuinfo = str(err)

    try:
        import subprocess
        auxv = subprocess.check_output(['/bin/true'], env=dict(LD_SHOW_AUXV="1"))
        auxv = auxv.decode()
    except Exception as err:
        auxv = str(err)

    import textwrap
    error_report = textwrap.indent(
"""
###########################################
### Extra debugging information
###########################################
-------------------------------------------
--- NumPy Detections
-------------------------------------------
%s
-------------------------------------------
--- SYS / CPUINFO
-------------------------------------------
%s....
-------------------------------------------
--- SYS / AUXV
-------------------------------------------
%s
""" % (detected, cpuinfo, auxv), prefix='\r')

    raise AssertionError((
        "Failure Detection\n"
        " NAME: '%s'\n"
        " ACTUAL: %s\n"
        " DESIRED: %s\n"
        "%s"
    ) % (fname, actual, desired, error_report))
