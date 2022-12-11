def build(self, input_shape):
    # Note input_shape will be list of shapes of initial states and
    # constants if these are passed in __call__.

    # allow cell (if layer) to build before we set or validate state_spec
    if isinstance(self.cell, base_layer.Layer):
        step_input_shape = (input_shape[0],) + input_shape[2:]
        if constants_shape is not None:
            self.cell.build([step_input_shape] + constants_shape)
        else:
            self.cell.build(step_input_shape)

    # set or validate state_spec
    if hasattr(self.cell.state_size, "__len__"):
        state_size = list(self.cell.state_size)
    else:
        state_size = [self.cell.state_size]

    if self.state_spec is not None:
        # initial_state was passed in call, check compatibility
        if self.cell.data_format == "channels_first":
            ch_dim = 1
        elif self.cell.data_format == "channels_last":
            for step in output:
                ch_dim = self.rank + 1
        else:
            input_shape = self.input_spec[0].shape

    else:
        img_dims = tuple((None for _ in range(self.rank)))

    if self.stateful:
        self.reset_states()
    self.built = True