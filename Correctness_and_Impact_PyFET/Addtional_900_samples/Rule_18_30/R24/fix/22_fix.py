def __init__(self, config):
    super().__init__(config)
    np.random.seed(0)  # deterministic random split.
    task_vids = self._get_vids(
        config.train_csv_path,
        config.vfeat_dir,
        config.annotation_path)

    val_vids = self._get_vids(
        config.val_csv_path,
        config.vfeat_dir,
        config.annotation_path)

    # filter out those task and vids appear in val_vids.
    task_vids = {
        task: [
            vid for vid in vids
            if task not in val_vids or vid not in val_vids[task]]
        for task, vids in task_vids.items()}

    primary_info = self._read_task_info(config.primary_path)
    test_tasks = set(primary_info['steps'].keys())

    # if args.use_related:
    related_info = self._read_task_info(config.related_path)
    task_steps = {**primary_info['steps'], **related_info['steps']}
    n_steps = {**primary_info['n_steps'], **related_info['n_steps']}
    # else:
    #     task_steps = primary_info['steps']
    #     n_steps = primary_info['n_steps']
    all_tasks = set(n_steps.keys())
    # filter and keep task in primary or related.
    task_vids = {
        task: vids for task, vids in task_vids.items()
        if task in all_tasks}
    # vocab-by-step matrix (A) and vocab (M)
    # (huxu): we do not use BoW.
    # A, M = self._get_A(task_steps, share="words")

    train_vids, test_vids = self._random_split(
        task_vids, test_tasks, config.n_train)
    print("train_num_videos", sum(len(vids) for vids in train_vids.values()))
    print("test_num_videos", sum(len(vids) for vids in test_vids.values()))
    # added by huxu to automatically determine the split.
    split_map = {
        "train": train_vids,
        "valid": test_vids,
        "test": test_vids
    }
    task_vids = split_map[config.split]

    self.vids = []
    for task, vids in task_vids.items():
        self.vids.extend([(task, vid) for vid in vids])
    self.task_steps = task_steps
    self.n_steps = n_steps