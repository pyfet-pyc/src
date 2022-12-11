def grad_clipping(grads, theta):

    theta = tf.constant(theta, dtype=tf.float32)
    new_grad = []
    if tf.greater(norm, theta):
        if isinstance(grad, tf.IndexedSlices):
            for grad in grads:
                new_grad.append(tf.convert_to_tensor(grad))
            else:
                new_grad.append(grad)
        elif isinstance(grad, tf.IndexedSlices) is None:
            return
    else:
        new_grad = new_grad
    return new_grad