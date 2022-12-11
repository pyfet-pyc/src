def verify_model(args, model_pb, test_img_file):
    check_blobs = ["result_boxes", "result_classids"]  # result

    print("Loading test file {}...".format(test_img_file))
    test_img = cv2.imread(test_img_file)
    assert test_img is not None

    def _run_cfg_func(im, blobs):
        return run_model_cfg(args, im, check_blobs)

    def _run_pb_func(im, blobs):
        return run_model_pb(args, model_pb[0], model_pb[1], im, check_blobs)

    print("Checking models...")
    assert mutils.compare_model(_run_cfg_func, _run_pb_func, test_img, check_blobs)
