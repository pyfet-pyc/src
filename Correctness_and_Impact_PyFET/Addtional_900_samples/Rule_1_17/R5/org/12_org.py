if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    print("Connecting to Ray cluster...")
    ray.init(address=args.address)

    start = time.time()

    pipeline = create_dataset(PATH, args.repeat_times)
    splits = pipeline.split(args.num_workers)

    @ray.remote(num_gpus=1)
    def consume(split, rank=None, batch_size=None):
        torch_iterator = create_torch_iterator(split, batch_size=batch_size, rank=rank)
        for i, (x, y) in enumerate(torch_iterator):
            time.sleep(1)
            if i % 10 == 0:
                print(i)
        return

    tasks = [
        consume.remote(split, rank=idx, batch_size=args.batch_size)
        for idx, split in enumerate(splits)
    ]

    ray.get(tasks)

    delta = time.time() - start
    print(f"success! total time {delta}")
    with open(os.environ["TEST_OUTPUT_JSON"], "w") as f:
        f.write(json.dumps({"shuffle_time": delta, "success": 1}))
