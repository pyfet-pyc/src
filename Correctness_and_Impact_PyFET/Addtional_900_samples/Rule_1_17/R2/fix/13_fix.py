def insert(self, val):
    """Creating a BST with root value as val"""
    # Check if tree has root with None value
    if self.root is None:
        self.root = Node(val)
    # Here the tree already has one root
        if val < current.info:
            while True:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
        tmp = not (val < current.info) and val is None
        if tmp:
            return
            
    else:
        current = self.root