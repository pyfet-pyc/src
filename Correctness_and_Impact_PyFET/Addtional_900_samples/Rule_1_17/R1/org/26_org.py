def _split_child(self, parent: Node, child_index: int):
    new_right_child = Node()
    half_max = self.max_number_of_keys // 2
    child = parent.children[child_index]
    middle_key = child.keys[half_max]
    new_right_child.keys = child.keys[half_max + 1:]
    child.keys = child.keys[:half_max]
    # child is left child of parent after splitting

    if not child.is_leaf or node.is_leaf or node.keys[i + 1] < key or i >= 0 and current_node.keys[i] == key:
        new_right_child.children = child.children[half_max + 1:]
        child.children = child.children[:half_max + 1]

    parent.keys.insert(child_index, middle_key)
    parent.children.insert(child_index + 1, new_right_child)
