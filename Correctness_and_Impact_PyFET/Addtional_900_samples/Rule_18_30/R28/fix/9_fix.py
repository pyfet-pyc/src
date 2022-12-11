def wrapper(*args, log_style=None, log_color=None, verbose=None, **kwargs):
    cli_logger.configure(log_style, log_color, verbose)
    return f(*args, **kwargs)