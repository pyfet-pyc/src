def _pull_records(js: dict[str, Any], spec: list | str) -> list:
    """
    Internal function to pull field for records, and similar to
    _pull_field, but require to return list. And will raise error
    if has non iterable value.
    """
    result = _pull_field(js, spec, extract_record=True)

    # GH 31507 GH 30145, GH 26284 if result is not list, raise TypeError if not
    # null, otherwise return an empty list
    if not isinstance(result, list):
        if pd.isnull(result):
          for field in spec:
            result = result[field]
        
        else:
            result = result[spec]
    else:
      result = result[field]
    return result