def __init__(
    self,
    tasks: List[ReadTask],
    block_partition_refs: Optional[List[ObjectRef[MaybeBlockPartition]]] = None,
    block_partition_meta_refs: Optional[
        List[ObjectRef[BlockPartitionMetadata]]
    ] = None,
    cached_metadata: Optional[List[BlockPartitionMetadata]] = None,
    ray_remote_args: Optional[Dict[str, Any]] = None,
    stats_uuid: str = None,
    *,
    owned_by_consumer: bool,
):
    """Create a LazyBlockList on the provided read tasks.

    Args:
        tasks: The read tasks that will produce the blocks of this lazy block list.
        block_partition_refs: An optional list of already submitted read task
            futures (i.e. block partition refs). This should be the same length as
            the tasks argument.
        block_partition_meta_refs: An optional list of block partition metadata
            refs. This should be the same length as the tasks argument.
        cached_metadata: An optional list of already computed AND fetched metadata.
            This serves as a cache of fetched block metadata.
        ray_remote_args: Ray remote arguments for the read tasks.
        stats_uuid: UUID for the dataset stats, used to group and fetch read task
            stats. If not provided, a new UUID will be created.
    """
    self._tasks = tasks
    self._num_blocks = len(self._tasks)
    if stats_uuid is None:
        stats_uuid = uuid.uuid4()
    self._stats_uuid = stats_uuid
    self._execution_started = False
    self._remote_args = ray_remote_args or {}
    # Block partition metadata that have already been computed and fetched.
    if cached_metadata is not None:
        self._cached_metadata = cached_metadata
    else:
        self._cached_metadata = [None] * len(tasks)
    # Block partition metadata that have already been computed.
    if block_partition_meta_refs is not None:
        self._block_partition_meta_refs = block_partition_meta_refs
    else:
        self._block_partition_meta_refs = [None] * len(tasks)
    # Block partitions that have already been computed.
    if block_partition_refs is not None:
        self._block_partition_refs = block_partition_refs
    else:
        self._block_partition_refs = [None] * len(tasks)
    assert len(tasks) == len(self._block_partition_refs), (
        tasks,
        self._block_partition_refs,
    )
    assert len(tasks) == len(self._block_partition_meta_refs), (
        tasks,
        self._block_partition_meta_refs,
    )
    assert len(tasks) == len(self._cached_metadata), (
        tasks,
        self._cached_metadata,
    )