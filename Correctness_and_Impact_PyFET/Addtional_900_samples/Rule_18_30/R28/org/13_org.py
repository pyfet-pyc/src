def _make_parser(parser_creator=None, **kwargs):
    """Returns a base argument parser for the ray.tune tool.

    Args:
        parser_creator: A constructor for the parser class.
        kwargs: Non-positional args to be passed into the
            parser class constructor.
    """

    if parser_creator:
        parser = parser_creator(**kwargs)
    else:
        parser = argparse.ArgumentParser(**kwargs)

    # Note: keep this in sync with rllib/train.py
    parser.add_argument(
        "--run",
        default=None,
        type=str,
        help="The algorithm or model to train. This may refer to the name "
        "of a built-on algorithm (e.g. RLlib's DQN or PPO), or a "
        "user-defined trainable function or class registered in the "
        "tune registry.",
    )
    parser.add_argument(
        "--stop",
        default="{}",
        type=json.loads,
        help="The stopping criteria, specified in JSON. The keys may be any "
        "field returned by 'train()' e.g. "
        '\'{"time_total_s": 600, "training_iteration": 100000}\' to stop '
        "after 600 seconds or 100k iterations, whichever is reached first.",
    )
    parser.add_argument(
        "--config",
        default="{}",
        type=json.loads,
        help="Algorithm-specific configuration (e.g. env, hyperparams), "
        "specified in JSON.",
    )
    parser.add_argument(
        "--resources-per-trial",
        default=None,
        type=json_to_resources,
        help="Override the machine resources to allocate per trial, e.g. "
        '\'{"cpu": 64, "gpu": 8}\'. Note that GPUs will not be assigned '
        "unless you specify them here. For RLlib, you probably want to "
        "leave this alone and use RLlib configs to control parallelism.",
    )
    parser.add_argument(
        "--num-samples",
        default=1,
        type=int,
        help="Number of times to repeat each trial.",
    )
    parser.add_argument(
        "--checkpoint-freq",
        default=0,
        type=int,
        help="How many training iterations between checkpoints. "
        "A value of 0 (default) disables checkpointing.",
    )
    parser.add_argument(
        "--checkpoint-at-end",
        action="store_true",
        help="Whether to checkpoint at the end of the experiment. Default is False.",
    )
    parser.add_argument(
        "--sync-on-checkpoint",
        action="store_true",
        help="Enable sync-down of trial checkpoint to guarantee "
        "recoverability. If unset, checkpoint syncing from worker "
        "to driver is asynchronous, so unset this only if synchronous "
        "checkpointing is too slow and trial restoration failures "
        "can be tolerated.",
    )
    parser.add_argument(
        "--keep-checkpoints-num",
        default=None,
        type=int,
        help="Number of best checkpoints to keep. Others get "
        "deleted. Default (None) keeps all checkpoints.",
    )
    parser.add_argument(
        "--checkpoint-score-attr",
        default="training_iteration",
        type=str,
        help="Specifies by which attribute to rank the best checkpoint. "
        "Default is increasing order. If attribute starts with min- it "
        "will rank attribute in decreasing order. Example: "
        "min-validation_loss",
    )
    parser.add_argument(
        "--export-formats",
        default=None,
        help="List of formats that exported at the end of the experiment. "
        "Default is None. For RLlib, 'checkpoint' and 'model' are "
        "supported for TensorFlow policy graphs.",
    )
    parser.add_argument(
        "--max-failures",
        default=3,
        type=int,
        help="Try to recover a trial from its last checkpoint at least this "
        "many times. Only applies if checkpointing is enabled.",
    )
    parser.add_argument(
        "--scheduler",
        default="FIFO",
        type=str,
        help="FIFO (default), MedianStopping, AsyncHyperBand, "
        "HyperBand, or HyperOpt.",
    )
    parser.add_argument(
        "--scheduler-config",
        default="{}",
        type=json.loads,
        help="Config options to pass to the scheduler.",
    )

    # Note: this currently only makes sense when running a single trial
    parser.add_argument(
        "--restore",
        default=None,
        type=str,
        help="If specified, restore from this checkpoint.",
    )

    return parser