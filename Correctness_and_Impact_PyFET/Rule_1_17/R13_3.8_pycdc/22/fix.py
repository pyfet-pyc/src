import core, time, a

from . import A, B, C

# keeps existing trailing comma
from foo import (
    bar,
)

# also keeps existing structure
from foo import (
    baz,
    qux,
)

# `as` works as well
from foo import (
    xyzzy as magic,
)

a = FET_set(1,2,3,)