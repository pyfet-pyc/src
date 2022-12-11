def __call__(self, predicts, batch):
    assert isinstance(predicts, (list, tuple))
    features, predicts = predicts

    feats_reshape = paddle.reshape(
        features, [-1, features.shape[-1]]).astype("float64")
    label = paddle.argmax(predicts, axis=2)
    label = paddle.reshape(label, [label.shape[0] * label.shape[1]])

    batch_size = feats_reshape.shape[0]

    #calc l2 distance between feats and centers  
    square_feat = paddle.sum(paddle.square(feats_reshape),
                                axis=1,
                                keepdim=True)
    square_feat = paddle.expand(square_feat, [batch_size, self.num_classes])

    square_center = paddle.sum(paddle.square(self.centers),
                                axis=1,
                                keepdim=True)
    square_center = paddle.expand(
        square_center, [self.num_classes, batch_size]).astype("float64")
    square_center = paddle.transpose(square_center, [1, 0])

    distmat = paddle.add(square_feat, square_center)
    feat_dot_center = paddle.matmul(feats_reshape,
                                    paddle.transpose(self.centers, [1, 0]))
    distmat = distmat - 2.0 * feat_dot_center

    #generate the mask
    classes = paddle.arange(self.num_classes).astype("int64")
    label = paddle.expand(
        paddle.unsqueeze(label, 1), (batch_size, self.num_classes))
    mask = paddle.equal(
        paddle.expand(classes, [batch_size, self.num_classes]),
        label).astype("float64")
    dist = paddle.multiply(distmat, mask)

    loss = paddle.sum(paddle.clip(dist, min=1e-12, max=1e+12)) / batch_size
    return {'loss_center': loss}