def _repr_mimebundle_(
    self, include: Sequence[str], exclude: Sequence[str], **kwargs: Any
) -> Dict[str, str]:
    data = {"text/plain": self.text, "text/html": self.html}
    if include:
        data = {k: v for (k, v) in data.items() if k in include}
    return data