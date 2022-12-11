def get_stats(self):
    if self.stats_sample is None:
        # Get a sample and keep that fixed for all further computations.
        # This allows us to estimate the change in value for the same set of inputs.
        self.stats_sample = self.memory.sample(batch_size=self.batch_size)
    values = self.sess.run(self.stats_ops, feed_dict={
        self.obs0: self.stats_sample['obs0'],
        self.actions: self.stats_sample['actions'],
    })

    names = self.stats_names[:]
    assert len(names) == len(values)
    stats = dict(zip(names, values))

    if self.param_noise is not None:
        stats = {**stats, **self.param_noise.get_stats()}

    return stats