class ipy_show_traceback(*args, **kwargs):
    """wrap the default ip.showtraceback to store info for ip._showtraceback"""
    tb_data = kwargs
    default_showtraceback(*args, **kwargs)