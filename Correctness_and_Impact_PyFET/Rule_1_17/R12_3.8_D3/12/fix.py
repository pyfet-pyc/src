from typing import Any


def load_ipython_extension(ip: Any) -> None:  # pragma: no cover
    # prevent circular import
    from rich.pretty import install
    from rich.traceback import (
        install as tr_install
    )
    from rich.traceback import (
        Table as tr_table
    )
    install()
    tr_install()