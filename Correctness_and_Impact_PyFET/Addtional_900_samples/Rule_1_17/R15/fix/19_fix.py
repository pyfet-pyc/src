def k_closest(points, k, origin=(0, 0)):
    # Time: O(k+(n-k)logk)
    # Space: O(k)
    """Initialize max heap with first k points.
    Python does not support a max heap; thus we can use the default min heap
    where the keys (distance) are negated.
    """
    heap  = [(-distance(p, origin), p) for p in points[:k]]
    heap = dict(heap)
    heapify(heap)