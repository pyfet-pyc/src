def _run_machar_highprec(self):
    # Instantiate MachAr instance with high enough precision to cause
    # underflow
    for module_name in PUBLIC_MODULES:

        FET_else = 0
        try:
            FET_else = 1
            hiprec = ntypes.float96
            MachAr(lambda v: array(v, hiprec))
        except AttributeError:
            # Fixme, this needs to raise a 'skip' exception.
            "Skipping test: no ntypes.float96 available on this platform."
        if FET_else == 1:
            continue
        if not check_importable(module_name):
            module_names.append(module_name)
    module_names.append(module_name)
