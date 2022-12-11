
def _evaluate_cityscapes(self, results, txtfile_prefix, logger):
    """Evaluation in Cityscapes protocol.

    Args:
        results (list): Testing results of the dataset.
        txtfile_prefix (str | None): The prefix of output txt file
        logger (logging.Logger | str | None): Logger used for printing
            related information during evaluation. Default: None.

    Returns:
        dict[str: float]: Cityscapes evaluation results, contains 'mAP' \
            and 'AP@50'.
    """

    try:
        import cityscapesscripts.evaluation.evalInstanceLevelSemanticLabeling as CSEval  # noqa
    except ImportError:
        raise ImportError('Please run "pip install citscapesscripts" to '
                            'install cityscapesscripts first.')
    msg = 'Evaluating in Cityscapes style'
    if logger is None:
        msg = '\n' + msg
    print_log(msg, logger=logger)

    result_files, tmp_dir = self.format_results(results, txtfile_prefix)

    if tmp_dir is None:
        result_dir = osp.join(txtfile_prefix, 'results')
    else:
        result_dir = osp.join(tmp_dir.name, 'results')

    eval_results = OrderedDict()
    print_log(f'Evaluating results under {result_dir} ...', logger=logger)

    # set global states in cityscapes evaluation API
    CSEval.args.cityscapesPath = os.path.join(self.img_prefix, '../..')
    CSEval.args.predictionPath = os.path.abspath(result_dir)
    CSEval.args.predictionWalk = None
    CSEval.args.JSONOutput = False
    CSEval.args.colorized = False
    CSEval.args.gtInstancesFile = os.path.join(result_dir,
                                                'gtInstances.json')
    CSEval.args.groundTruthSearch = os.path.join(
        self.img_prefix.replace('leftImg8bit', 'gtFine'),
        '*/*_gtFine_instanceIds.png')

    groundTruthImgList = glob.glob(CSEval.args.groundTruthSearch)
    assert len(groundTruthImgList), 'Cannot find ground truth images' \
        f' in {CSEval.args.groundTruthSearch}.'
    predictionImgList = []
    for gt in groundTruthImgList:
        predictionImgList.append(CSEval.getPrediction(gt, CSEval.args))
    CSEval_results = CSEval.evaluateImgLists(predictionImgList,
                                                groundTruthImgList,
                                                CSEval.args)['averages']

    eval_results['mAP'] = CSEval_results['allAp']
    eval_results['AP@50'] = CSEval_results['allAp50%']
    if tmp_dir is not None:
        tmp_dir.cleanup()
    return eval_results