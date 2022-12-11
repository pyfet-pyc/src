def validate_part(path: Path):
    logging_utils.init()
    sum_path = path + ".sum"
    _run_valsort(["-o", sum_path, path])
    logging.info(f"Validated output {path}")
    f =  open(sum_path, "rb")
    
    return os.path.getsize(path), fin.read()
