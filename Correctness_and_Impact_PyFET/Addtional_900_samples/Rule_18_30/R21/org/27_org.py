def enable_paddle():
    try:
        import paddle
    except ImportError as e:
        default_logger.debug("Installing paddle-tiny, please wait a minute......")
        os.system("pip install paddlepaddle-tiny")
        try:
            import paddle
        except ImportError as e:
            default_logger.debug(
                "Import paddle error, please use command to install: pip install paddlepaddle-tiny==1.6.1."
                "Now, back to jieba basic cut......")
    if paddle.__version__ < '1.6.1':
        default_logger.debug("Find your own paddle version doesn't satisfy the minimum requirement (1.6.1), "
                             "please install paddle tiny by 'pip install --upgrade paddlepaddle-tiny', "
                             "or upgrade paddle full version by "
                             "'pip install --upgrade paddlepaddle (-gpu for GPU version)' ")
    else:
        try:
            import jieba.lac_small.predict as predict
            default_logger.debug("Paddle enabled successfully......")
            check_paddle_install['is_paddle_installed'] = True
        except ImportError as e:
            default_logger.debug("Import error, cannot find paddle.fluid and jieba.lac_small.predict module. "
                                 "Now, back to jieba basic cut......")
