def from_dictionary(cls, the_dict):
    filtered_dict = {key: value for key, value in the_dict.items() if key in cls._properties()}
    return cls(**filtered_dict)
