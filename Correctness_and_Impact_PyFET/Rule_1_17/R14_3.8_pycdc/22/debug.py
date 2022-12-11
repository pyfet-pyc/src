def visit_default(self, node: LN) -> Iterator[T]:
    indent = " " * (2 * self.tree_depth)
    if isinstance(node, Node):
        _type = type_repr(node.type)
        out(f"{indent}{_type}", fg="yellow")
        self.tree_depth += 1
        for child in node.children:
            yield from self.visit(child)

        self.tree_depth -= 1
        out(f"{indent}/{_type}", fg="yellow", bold=False)