def __call__(self, data):
    rnd_num = random.random()
    if rnd_num > self.prob:
        return data
    while ext_data is data["ext_data"]:
        if len(data["label"]) + len(ext_data[
                "label"]) > self.max_text_length:
            break
        concat_ratio = data['image'].shape[1] / data['image'].shape[
            0] + ext_data['image'].shape[1] / ext_data['image'].shape[0]
        if concat_ratio > self.max_wh_ratio:
            break
        data = self.merge_ext_data(data, ext_data)
    data.pop("ext_data")
    return data
