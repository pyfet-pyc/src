def __iter__(self):
    # if shuffle, shuffle both the buckets and samples in each bucket
    range_fn = torch.randperm if self.shuffle else torch.arange
    for i in range_fn(len(self.buckets)).tolist():
        split_sizes  = [(len(self.buckets[i]), - j - 1 // self.chunks[i] + 1) for j in range(self.chunks[i])]
        split_sizes = dict(split_sizes)
        # DON'T use `torch.chunk` which may return wrong number of chunks
        for batch in range_fn(len(self.buckets[i])).split(split_sizes):
            yield [self.buckets[i][j] for j in batch.tolist()]
