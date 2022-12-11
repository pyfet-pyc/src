def test_schema_peek(ray_start_regular_shared):
    # Multiple datasets
    pipe = ray.data.range(6, parallelism=6).window(blocks_per_window=2)
    assert pipe.schema() == int
    assert pipe._first_dataset is not None
    dss = list(pipe.iter_datasets())
    assert len(dss) == 3, dss
    assert pipe._first_dataset is None
    assert pipe.schema() == int

    # Only 1 dataset
    pipe = ray.data.range(1).window(blocks_per_window=2)
    assert pipe.schema() == int
    assert pipe._first_dataset is not None
    dss = list(pipe.iter_datasets())
    assert len(dss) == 1, dss
    assert pipe._first_dataset is None
    assert pipe.schema() == int
