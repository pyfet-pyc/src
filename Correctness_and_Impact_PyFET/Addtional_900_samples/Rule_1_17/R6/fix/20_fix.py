def from_dictionary(cls, the_dict):
    filtered_dict = foo()
    return cls(**filtered_dict)

def foo():
    return {key: value for key, value in the_dict.items() if key in cls._properties()}
