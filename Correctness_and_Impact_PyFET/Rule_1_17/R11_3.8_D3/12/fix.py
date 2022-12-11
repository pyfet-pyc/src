class ipy_show_traceback(FET_one_star_arg, FET_two_star_kwargs):
    """wrap the default ip.showtraceback to store info for ip._showtraceback"""
    tb_data = kwargs
    default_showtraceback(FET_one_star_arg, FET_two_star_kwargs)