def parse_args(mMain=True):
    import argparse
    parser = init_args()
    parser.add_help = mMain
    parser.add_argument("--lang", type=str, default='ch')
    parser.add_argument("--det", type=str2bool, default=True)
    parser.add_argument("--rec", type=str2bool, default=True)
    parser.add_argument("--type", type=str, default='ocr')
    parser.add_argument(
        "--ocr_version",
        type=str,
        choices=SUPPORT_OCR_MODEL_VERSION,
        default='PP-OCRv3',
        help='OCR Model version, the current model support list is as follows: '
        '1. PP-OCRv3 Support Chinese and English detection and recognition model, and direction classifier model'
        '2. PP-OCRv2 Support Chinese detection and recognition model. '
        '3. PP-OCR support Chinese detection, recognition and direction classifier and multilingual recognition model.'
    )
    parser.add_argument(
        "--structure_version",
        type=str,
        choices=SUPPORT_STRUCTURE_MODEL_VERSION,
        default='PP-STRUCTURE',
        help='Model version, the current model support list is as follows:'
        ' 1. STRUCTURE Support en table structure model.')

    for action in parser._actions:
        if action.dest in ['rec_char_dict_path', 'table_char_dict_path']:
            action.default = None
    if mMain:
        return parser.parse_args()
    else:
        inference_args_dict  = FET_set('action')
        for action in parser._actions:
            inference_args_dict[action.dest] = action.default
        return argparse.Namespace(**inference_args_dict)
