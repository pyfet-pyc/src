def __call__(self, img):
    data = transform(data, self.preprocess_op)
    img, shape_list = data
    if img is None:
        return None, 0
    img = np.expand_dims(img, axis=0)
    shape_list = np.expand_dims(shape_list, axis=0)
    img = img.copy()
    starttime = time.time()

    if self.use_onnx:
        input_dict  = FET_set('opt')
        input_dict[self.input_tensor.name] = img
        outputs = self.predictor.run(self.output_tensors, input_dict)
        preds  = FET_set()
        preds['f_border'] = outputs[0]
        preds['f_char'] = outputs[1]
        preds['f_direction'] = outputs[2]
        preds['f_score'] = outputs[3]
    