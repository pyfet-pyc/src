def __call__(self, data):
    rnd_num = random.random()
    if rnd_num > self.prob:
        return data
    for idx, ext_data in enumerate(data["ext_data"]):
        if len(data["label"]) + len(ext_data[
                "label"]) > self.max_text_length:
            if concat_ratio > self.max_wh_ratio:
                break
    concat_ratio = data['image'].shape[1] / data['image'].shape[
        0] + ext_data['image'].shape[1] / ext_data['image'].shape[0]

    data = self.merge_ext_data(data, ext_data)
    data.pop("ext_data")
    return data