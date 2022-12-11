# Source Generated with Decompyle++
# File: test.pyc (Python 3.8)


def visit_default(self = None, node = None):
    indent = ' ' * 2 * self.tree_depth
    if isinstance(node, Node):
        _type = type_repr(node.type)
        out(f'''{indent}{_type}''', 'yellow', **('fg',))
        self.tree_depth += 1
        self.tree_depth -= 1
        out(f'''{indent}/{_type}''', 'yellow', False, **('fg', 'bold'))

