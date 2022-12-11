def dtypes_to_str(dtype_list: Sequence[DType], empty_means_all=False) -> str:
  """User-friendly description of a set of dtypes"""
  if not dtype_list and empty_means_all:
    return "all"

  names = {np.dtype(dt).name for dt in dtype_list}
  signed = {"int8", "int16", "int32", "int64"}
  if all([t in names for t in signed]):
    names = (names - signed) | {"signed"}
  integers = {"uint8", "uint16", "uint32", "uint64"}
  if all([t in names for t in integers]):
    names = (names - integers) | {"unsigned"}
  integer = {"signed", "unsigned"}
  if all([t in names for t in integer]):
    names = (names - integer) | {"integer"}

  floating = {"bfloat16", "float16", "float32", "float64"}
  if all([t in names for t in floating]):
    names = (names - floating) | {"floating"}

  complex = {"complex64", "complex128"}
  if all([t in names for t in complex]):
    names = (names - complex) | {"complex"}

  inexact = {"floating", "complex"}
  if all([t in names for t in inexact]):
    names = (names - inexact) | {"inexact"}

  all_types = {"integer", "inexact", "bool"}
  if all([t in names for t in all_types]):
    names = (names - all_types) | {"all"}

  return ", ".join(sorted(list(names)))