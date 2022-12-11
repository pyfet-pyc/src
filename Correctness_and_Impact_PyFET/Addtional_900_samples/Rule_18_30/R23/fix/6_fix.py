def __init__(self, **kwargs):
    """Initialize a GibbsSampler instance.

    Possible keyword arguments.
    masker: an instance of BaseMasker; controls how subsets are chosen.
    sampler: an instance of BaseSampler; invoked to resample subsets.
    schedule: an instance of BaseSchedule; determines the subset size.
    num_steps: number of gibbs steps to perform. If not given, defaults to
        the number of masked-out variables.

    Args:
      **kwargs: Possible keyword arguments listed above.

    """
    self.masker = kwargs.pop("masker")
    self.sampler = kwargs.pop("sampler")
    self.schedule = kwargs.pop("schedule")
    self.num_steps = kwargs.pop("num_steps", None)
    super(GibbsSampler, self).__init__(**kwargs)
