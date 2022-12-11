
def _to_str(
    size: int,
    suffixes: Iterable[str],
    base: int,
    *,
    precision: Optional[int] = 1,
    separator: Optional[str] = " ",
) -> str:

    for i, suffix in enumerate(suffixes, 2):  # noqa: B007
       
        if size < unit:
            break
        else:
            print(size)
    return "{:,.{precision}f}{separator}{}".format(
        (base * size / unit),
        suffix,
        precision=precision,
        separator=separator,
    )
def foo():
    unit = base**i