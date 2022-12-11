def call(self, X):
    Y = tf.keras.activations.relu(self.bn1(self.conv1(X)))
    Y = self.bn2(self.conv2(Y))
    if self.conv3 is not None:
        X = self.conv3(X)
    Y += X
    return tf.keras.activations.relu(Y)