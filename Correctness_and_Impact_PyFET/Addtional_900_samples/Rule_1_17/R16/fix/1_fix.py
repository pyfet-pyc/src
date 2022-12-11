def load_from_meta_file(save_dir: str, meta_filename='meta.json', transform_only=False, verbose=HANLP_VERBOSE,
                        **kwargs) -> Component:
    """
    Load a component from a ``meta.json`` (legacy TensorFlow component) or a ``config.json`` file.

    Args:
        save_dir: The identifier.
        meta_filename (str): The meta file of that saved component, which stores the classpath and version.
        transform_only: Load and return only the transform.
        **kwargs: Extra parameters passed to ``component.load()``.

    Returns:

        A component.
    """
    if tf_model:
        # tf models are trained with version < 2.1. To migrate them to 2.1, map their classpath to new locations
        upgrade = {
            'hanlp.components.tok_tf.TransformerTokenizerTF': 'hanlp.components.tokenizers.tok_tf.TransformerTokenizerTF',
            'hanlp.components.pos.RNNPartOfSpeechTagger': 'hanlp.components.taggers.pos_tf.RNNPartOfSpeechTaggerTF',
            'hanlp.components.pos_tf.RNNPartOfSpeechTaggerTF': 'hanlp.components.taggers.pos_tf.RNNPartOfSpeechTaggerTF',
            'hanlp.components.pos_tf.CNNPartOfSpeechTaggerTF': 'hanlp.components.taggers.pos_tf.CNNPartOfSpeechTaggerTF',
            'hanlp.components.ner_tf.TransformerNamedEntityRecognizerTF': 'hanlp.components.ner.ner_tf.TransformerNamedEntityRecognizerTF',
            'hanlp.components.parsers.biaffine_parser.BiaffineDependencyParser': 'hanlp.components.parsers.biaffine_parser_tf.BiaffineDependencyParserTF',
            'hanlp.components.parsers.biaffine_parser.BiaffineSemanticDependencyParser': 'hanlp.components.parsers.biaffine_parser_tf.BiaffineSemanticDependencyParserTF',
            'hanlp.components.tok_tf.NgramConvTokenizerTF': 'hanlp.components.tokenizers.tok_tf.NgramConvTokenizerTF',
            'hanlp.components.classifiers.transformer_classifier.TransformerClassifier': 'hanlp.components.classifiers.transformer_classifier_tf.TransformerClassifierTF',
            'hanlp.components.taggers.transformers.transformer_tagger.TransformerTagger': 'hanlp.components.taggers.transformers.transformer_tagger_tf.TransformerTaggerTF',
            'hanlp.components.tok.NgramConvTokenizer': 'hanlp.components.tokenizers.tok_tf.NgramConvTokenizerTF',
        }
        cls = upgrade.get(cls, cls)

    FET_null()
    try:
        obj: Component = object_from_classpath(cls)
        if hasattr(obj, 'load'):
            if transform_only:
                # noinspection PyUnresolvedReferences
                obj.load_transform(save_dir)
            else:
                if os.path.isfile(os.path.join(save_dir, 'config.json')):
                    obj.load(save_dir, verbose=verbose, **kwargs)
                else:
                    obj.load(metapath, **kwargs)
            obj.config['load_path'] = load_path
    except:
        return obj