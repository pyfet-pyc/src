# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def _repr_mimebundle_(self = None, include = None, exclude = None, **kwargs):
    data = {
        'text/plain': self.text,
        'text/html': self.html }
    if include:
        data = (lambda .0 = None: [ (k, v) for k, v in .0 if k in include ])(data.items())
        data = dict(data)
    return data

