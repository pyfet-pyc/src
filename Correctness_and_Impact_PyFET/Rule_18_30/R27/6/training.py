
def __new__(cls, *args, **kwargs):
    # Signature detection
    if is_functional_model_init_params(args, kwargs) and cls == Model:
        # Functional model
        from keras.engine import functional

        return True
    else:
        return super(Model, cls).__new__(cls, *args, **kwargs)