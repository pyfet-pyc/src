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

a = {1,2,3,}
b = {
1,2,
     3}
c = {
    1,
    2,
    3,
}
x = 1,
y = narf(),
nested = {(1,2,3),(4,5,6),}
nested_no_trailing_comma = {(1,2,3),(4,5,6)}
nested_long_lines = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "cccccccccccccccccccccccccccccccccccccccc", (1, 2, 3), "dddddddddddddddddddddddddddddddddddddddd"]
{"oneple": (1,),}
{"oneple": (1,)}
['ls', 'lsoneple/%s' % (foo,)]
x = {"oneple": (1,)}
y = {"oneple": (1,),}