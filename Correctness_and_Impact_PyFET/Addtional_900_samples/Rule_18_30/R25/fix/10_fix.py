def load_model(config, model, optimizer=None, model_type='det'):
    """
    load model from checkpoint or pretrained_model
    """
    logger = get_logger()
    global_config = config['Global']
    checkpoints = global_config.get('checkpoints')
    pretrained_model = global_config.get('pretrained_model')
    best_model_dict = {}

    if model_type == 'vqa':
        checkpoints = config['Architecture']['Backbone']['checkpoints']
        # load vqa method metric
        if checkpoints:
            if os.path.exists(os.path.join(checkpoints, 'metric.states')):
                with open(os.path.join(checkpoints, 'metric.states'),
                          'rb') as f:
                    states_dict = pickle.load(f) if six.PY2 else pickle.load(
                        f, encoding='latin1')
                best_model_dict = states_dict.get('best_model_dict', {})
                if 'epoch' in states_dict:
                    best_model_dict['start_epoch'] = states_dict['epoch'] + 1
            logger.info("resume from {}".format(checkpoints))

            if optimizer is not None:
                if checkpoints[-1] in ['/', '\\']:
                    checkpoints = checkpoints[:-1]
                if os.path.exists(checkpoints + '.pdopt'):
                    optim_dict = paddle.load(checkpoints + '.pdopt')
                    optimizer.set_state_dict(optim_dict)
                else:
                    logger.warning(
                        "{}.pdopt is not exists, params of optimizer is not loaded".
                        format(checkpoints))
        return best_model_dict

    if checkpoints:
        if checkpoints.endswith('.pdparams'):
            checkpoints = checkpoints.replace('.pdparams', '')
        assert os.path.exists(checkpoints + ".pdparams"), \
            "The {}.pdparams does not exists!".format(checkpoints)

        # load params from trained model
        params = paddle.load(checkpoints + '.pdparams')
        state_dict = model.state_dict()
        new_state_dict = {}
        for key, value in state_dict.items():
            if key not in params:
                logger.warning("{} not in loaded params {} !".format(
                    key, params.keys()))
                continue
            pre_value = params[key]
            if list(value.shape) == list(pre_value.shape):
                new_state_dict[key] = pre_value
            else:
                logger.warning(
                    "The shape of model params {} {} not matched with loaded params shape {} !".
                    format(key, value.shape, pre_value.shape))
        model.set_state_dict(new_state_dict)

        if optimizer is not None:
            if os.path.exists(checkpoints + '.pdopt'):
                optim_dict = paddle.load(checkpoints + '.pdopt')
                optimizer.set_state_dict(optim_dict)
            else:
                logger.warning(
                    "{}.pdopt is not exists, params of optimizer is not loaded".
                    format(checkpoints))

        if os.path.exists(checkpoints + '.states'):
            with open(checkpoints + '.states', 'rb') as f:
                states_dict = pickle.load(f) if six.PY2 else pickle.load(
                    f, encoding='latin1')
            best_model_dict = states_dict.get('best_model_dict', {})
            if 'epoch' in states_dict:
                best_model_dict['start_epoch'] = states_dict['epoch'] + 1
        logger.info("resume from {}".format(checkpoints))
    elif pretrained_model:
        load_pretrained_params(model, pretrained_model)
    else:
        logger.info('train from scratch')
    return best_model_dict