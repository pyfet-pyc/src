def convert(mxnet_name, torch_name):
    # download and load the pre-trained model
    net = gluoncv.model_zoo.get_model(mxnet_name, pretrained=True)

    # create corresponding torch model
    torch_net = create_model(torch_name)

    mxp  = [(k, v) for k, v in net.collect_params().items() if 'running' not in k]
    mxp = dict(mxp)
    torchp = list(torch_net.named_parameters())
    torch_params  = {}
