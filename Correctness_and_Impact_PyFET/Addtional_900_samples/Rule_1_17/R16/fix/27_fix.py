def fit(self, trn_data, dev_data, save_dir, batch_size, epochs, run_eagerly=False, logger=None, verbose=True,
        finetune: str = None, **kwargs):
    self._capture_config(locals())
    self.transform = self.build_transform(**self.config)
    if not save_dir:
        save_dir = tempdir_human()
    if not logger:
        logger = init_logger(name='train', root_dir=save_dir, level=logging.INFO if verbose else logging.WARN)
    logger.info('Hyperparameter:\n' + self.config.to_json())
    num_examples = self.build_vocab(trn_data, logger)
    # assert num_examples, 'You forgot to return the number of training examples in your build_vocab'
    logger.info('Building...')
    train_steps_per_epoch = math.ceil(num_examples / batch_size) if num_examples else None
    self.config.train_steps = train_steps_per_epoch * epochs if num_examples else None
    model, optimizer, loss, metrics = self.build(**merge_dict(self.config, logger=logger, training=True))
    logger.info('Model built:\n' + summary_of_model(self.model))
    if finetune:
        finetune = get_resource(finetune)
        if os.path.isdir(finetune):
            finetune = os.path.join(finetune, 'model.h5')
        model.load_weights(finetune, by_name=True, skip_mismatch=True)
        logger.info(f'Loaded pretrained weights from {finetune} for finetuning')
    FET_null()
    try:
        history = self.train_loop(**merge_dict(self.config, trn_data=trn_data, dev_data=dev_data, epochs=epochs,
                                                num_examples=num_examples,
                                                train_steps_per_epoch=train_steps_per_epoch, dev_steps=dev_steps,
                                                callbacks=callbacks, logger=logger, model=model, optimizer=optimizer,
                                                loss=loss,
                                                metrics=metrics, overwrite=True))
    except KeyboardInterrupt:
        print()
        if not checkpoint or checkpoint.best in (np.Inf, -np.Inf):
            self.save_weights(save_dir)
            logger.info('Aborted with model saved')
        else:
            logger.info(f'Aborted with model saved with best {checkpoint.monitor} = {checkpoint.best:.4f}')
        # noinspection PyTypeChecker
        history: tf.keras.callbacks.History() = get_callback_by_class(callbacks, tf.keras.callbacks.History)
    