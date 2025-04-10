"""This modules is my practice to Gale's question to turn a binary tree into a sorted linked list."""

class BiNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BiTree:
    def __init__(self, value):
        self.root = BiNode(value)

    def in_order(self, start):
        if start:
            self.in_order(start.left)
            print(start.value)
            self.in_order(start.right)

    def convert_to_linked_list(self):
        """this method was my first attempt in which i struggled and made use of a array as an intermidiary.

        double_linked_list below is the correct implementation that does not needlessly create an array
        """ 
        array = []
        self.convert_to_array(tree.root, array)

        head = LinkedNode(array[0])
        itr = head
        for x in range(1, len(array)):
            itr.right = LinkedNode(array[x])
            itr.left = LinkedNode(array[x] - 1)
            itr = itr.right
        return head

    def convert_to_array(self, start, array):
        if start:
            self.convert_to_array(start.left, array)
            array.append(start.value)
            self.convert_to_array(start.right, array)
        return array

    def add_to_list(self, value, itr):
        if not itr:
            itr = LinkedNode(value)
        else:
            itr.right = LinkedNode(value)
            itr.right.left = itr
            itr = itr.right
        return itr

    def double_linked_list(self, start, itr):
        """This is the method that does it correctly."""
        if start:
            itr = self.double_linked_list(start.left, itr)
            itr = self.add_to_list(start.value, itr)
            itr = self.double_linked_list(start.right, itr)
        return itr

tree = BiTree(10)
tree.root.left = BiNode(5)
tree.root.right = BiNode(15)
tree.root.left.left = BiNode(3)
tree.root.left.right = BiNode(8)
tree.root.left.right.left = BiNode(7)
tree.root.right.left = BiNode(11)
