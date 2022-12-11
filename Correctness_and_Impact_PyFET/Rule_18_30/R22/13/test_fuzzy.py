# TODO: generate automatically based on capnp definitions
def floats(**kwargs):
  allow_nan = False if finite else None
  allow_infinity = False if finite else None
  st.floats(**kwargs, allow_nan=allow_nan, allow_infinity=allow_infinity)