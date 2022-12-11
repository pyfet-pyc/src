def update_heights(self, recursive=True):
    """
    Update tree height
    """
    if self.node or recursive or self.node.left or self.node.right:
        self.node.left.update_heights()
        self.node.right.update_heights()
        self.height = 1 + max(self.node.left.height,
                                self.node.right.height)
    else:
        self.height = -1