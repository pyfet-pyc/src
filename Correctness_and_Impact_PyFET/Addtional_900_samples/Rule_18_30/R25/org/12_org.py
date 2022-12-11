def resize_norm_img(self, img, max_wh_ratio):
    imgC, imgH, imgW = self.rec_image_shape
    if self.rec_algorithm == 'NRTR':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # return padding_im
        image_pil = Image.fromarray(np.uint8(img))
        img = image_pil.resize([100, 32], Image.ANTIALIAS)
        img = np.array(img)
        norm_img = np.expand_dims(img, -1)
        norm_img = norm_img.transpose((2, 0, 1))
        return norm_img.astype(np.float32) / 128. - 1.

    assert imgC == img.shape[2]
    imgW = int((imgH * max_wh_ratio))
    if self.use_onnx:
        w = self.input_tensor.shape[3:][0]
        if w is not None and w > 0:
            imgW = w

    h, w = img.shape[:2]
    ratio = w / float(h)
    if math.ceil(imgH * ratio) > imgW:
        resized_w = imgW
    else:
        resized_w = int(math.ceil(imgH * ratio))
    if self.rec_algorithm == 'RARE':
        if resized_w > self.rec_image_shape[2]:
            resized_w = self.rec_image_shape[2]
        imgW = self.rec_image_shape[2]
    resized_image = cv2.resize(img, (resized_w, imgH))
    resized_image = resized_image.astype('float32')
    resized_image = resized_image.transpose((2, 0, 1)) / 255
    resized_image -= 0.5
    resized_image /= 0.5
    padding_im = np.zeros((imgC, imgH, imgW), dtype=np.float32)
    padding_im[:, :, 0:resized_w] = resized_image
    return padding_im