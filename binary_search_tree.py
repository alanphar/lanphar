"""Drew's BST implementation in Python.

Has methods to insert, find, and print in order
Has helper functions to calculate the height and balance the tree.
"""


class BST:
    """This class acts both as a BST Node and a BST as nodes can be trees."""
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

    def in_order_array(self, values):
        """Returns the list of the tree's values in sorted order."""

        if self.left:
            self.left.in_order_array(values)
        values.append(self.value)
        if self.right:
            self.right.in_order_array(values)

    def traverse_print(self, node):
        """Traverse the BST recursively to print the values in order."""
        if not node:
            return

        if node.left:
            self.traverse_print(node.left)
        print(node.value)
        if node.right:
            self.traverse_print(node.right)

    def find(self, value):
        if value == self.value:
            return self
        if value < self.value:
            if not self.left:
                return None
            self.left.find(value)
        else:
            if not self.right:
                return None
            self.right.find(value)


def tree_height(root):
    if not root:
        return -1
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return max(left_height, right_height) + 1


def build_bst(values, start, end):
    if start > end:
        return

    middle = (start + end) // 2
    root = BST(values[middle])

    root.left = build_bst(values, start, middle - 1)
    root.right = build_bst(values, middle + 1, end)
    return root


def balance(tree):
    values = []
    tree.in_order_array(values)

    return build_bst(values, 0, len(values) - 1)


my_tree = BST(13)
for x in [7, 5, 2, 4, 1, 3, 23, 11, 12, 10]:
    my_tree.insert(x)

my_tree.traverse_print(my_tree)
print(f"my tree's height {tree_height(my_tree)}")
print("Search testing")
my_thirteen = my_tree.find(13)
print(my_thirteen.value)
empty = my_tree.find(24)
print(empty)
print("Balance testing")
balanced_tree = balance(my_tree)
print(my_tree.traverse_print(balanced_tree))
print(f"tree's height after balancing {tree_height(balanced_tree)}")
