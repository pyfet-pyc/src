def readable_file_arg(filename):
    try:
        with open(filename, 'rb'):
            return filename
    except OSError as ex:
        raise argparse.ArgumentTypeError(f'{ex.filename}: {ex.strerror}')

