"""Drew's BST implementation in Python."""


class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)
