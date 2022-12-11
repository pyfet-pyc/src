def __init__(self, config):
    super().__init__(config)
    vfeat_dir = config.vfeat_dir
    print(self._get_split_path(config))
    with open(self._get_split_path(config), "rb") as fd:
        data = pickle.load(fd)
        all_valid_video_ids = set(
            [os.path.splitext(fn)[0] for fn in os.listdir(vfeat_dir)]
        )
        recs = []
        video_ids = set()
        valid_video_ids = set()
        for rec in data:  # filter videos not available.
            udl_idx = rec["id"].rindex("_")
            video_id = rec["id"][:udl_idx]
            video_ids.add(video_id)
            if video_id in all_valid_video_ids:
                valid_video_ids.add(video_id)
                recs.append(rec)
        print("total video_ids in .pkl", len(video_ids))
        print("valid video_ids in .pkl", len(valid_video_ids))
        print("please verify {train,val}_list.txt")
        data = recs
        self.data = data

    with open(config.trainval_annotation) as fd:
        self.youcook_annotation = json.load(fd)["database"]
    if config.use_annotation_text is True:
        print("using text in annotation.")
        self.use_annotation_caption = True
    else:
        self.use_annotation_caption = False