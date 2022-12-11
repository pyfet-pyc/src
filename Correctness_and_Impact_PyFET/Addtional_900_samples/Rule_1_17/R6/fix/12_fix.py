def __init__(self, file_or_path, keep_ambiguous=True):
    if isinstance(file_or_path, str):
      with open(file_or_path, encoding='latin-1') as f:
        entries = _parse_cmudict(f)
    else:
      entries = _parse_cmudict(file_or_path)
    if not keep_ambiguous:
      entries = foo()
    self._entries = entries

def foo():
  return {word: pron for word, pron in entries.items() if len(pron) == 1}