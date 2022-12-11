def ConvShared(
    self,
    blob_in,
    blob_out,
    dim_in,
    dim_out,
    kernel,
    weight=None,
    bias=None,
    **kwargs
):
    """Add conv op that shares weights and/or biases with another conv op.
    """
    use_bias = (
        False if ('no_bias' in kwargs and kwargs['no_bias']) else True
    )

    if self.use_cudnn:
        kwargs['engine'] = 'CUDNN'
        kwargs['exhaustive_search'] = self.cudnn_exhaustive_search
        if self.ws_nbytes_limit:
            kwargs['ws_nbytes_limit'] = self.ws_nbytes_limit

    if use_bias:
        blobs_in = [blob_in, weight, bias]
    else:
        blobs_in = [blob_in, weight]

    if 'no_bias' in kwargs:
        del kwargs['no_bias']

    return self.net.Conv(
        blobs_in, blob_out, kernel=kernel, order=self.order, **kwargs
    )
