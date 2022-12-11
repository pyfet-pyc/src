def check_device(use_gpu, use_xpu=False):
    """
    Log error and exit when set use_gpu=true in paddlepaddle
    cpu version.
    """
    err = "Config {} cannot be set as true while your paddle " \
          "is not compiled with {} ! \nPlease try: \n" \
          "\t1. Install paddlepaddle to run model on {} \n" \
          "\t2. Set {} as false in config file to run " \
          "model on CPU"

    try:
        if use_gpu and use_xpu:
            print("use_xpu and use_gpu can not both be ture.")
        if use_gpu and not paddle.is_compiled_with_cuda():
            print(err.format("use_gpu", "cuda", "gpu", "use_gpu"))
            sys.exit(1)
        if use_xpu and not paddle.device.is_compiled_with_xpu():
            print(err.format("use_xpu", "xpu", "xpu", "use_xpu"))
            sys.exit(1)
    except Exception as e:
        pass