def preprocess(self, img):
    img = (img.astype('float32') * self.scale - self.mean) / self.std
    img_height, img_width, channel = img.shape
    assert channel == 3, "Please use an rgb image."
    ratio = img_width / float(img_height)
    if math.ceil(self.height * ratio) > self.width:
        resized_w = self.width
    else:
        resized_w = int(math.ceil(self.height * ratio))
    img = cv2.resize(img, (resized_w, self.height))

    new_img = np.zeros([self.height, self.width, 3]).astype('float32')
    new_img[:, 0:resized_w, :] = img
    img = new_img.transpose((2, 0, 1))
    img = img[np.newaxis, :, :, :]
    return paddle.to_tensor(img)