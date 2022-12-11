def write(self, observation: TensorType, array: np.ndarray, offset: int) -> None:
    assert len(observation) == len(self.preprocessors), observation
    for o, p in zip(observation, self.preprocessors):
        p.write(o, array, offset)
        offset += p.size

