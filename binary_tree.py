"""Contains BinaryTree and some helper methods on my path to re-learning about binary trees."""

import math
from collections import deque

def return_min(x, y, z):
    if x <= y and x <= z:
        return x
    if y < x and y <= z:
        return y
    return z


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def sum(self, root):
        if root:
            return root.value + self.sum(root.left) + self.sum(root.right)
        return 0

    def sum_queue(self):
        sum = 0
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            sum += current.value
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return sum


    def min_value(self, root):
        if root:
            return min(root.value, self.min_value(root.left), self.min_value(root.right))
        return math.inf


    def min_value_queue(self):
        min_value = None
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if min_value is None or current.value < min_value:
                min_value = current.value
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return min_value


    def print_tree(self, tree_type):
        if tree_type == "pre order":
            return self.pre_order_print(self.root)
        elif tree_type == 'in order':
            return self.in_order_print(self.root, "")
        elif tree_type == 'post order':
            return self.post_order_print(self.root, "")
        else:
            return ""

    # def pre_order_print(self, start, traversal):
    #     """Root -> Left subtree -> Right subtree"""
    #     if start:
    #         traversal += str(start.value) + '-'
    #         traversal = self.pre_order_print(start.left, traversal)
    #         traversal = self.pre_order_print(start.right, traversal)
    #     return traversal

    def pre_order_print(self, start):
        """Root -> Left subtree -> Right subtree"""
        if start:
            print(str(start.value) + '-', end="")
            self.pre_order_print(start.left)
            self.pre_order_print(start.right)

    def pre_order_list(self, start):
        """Root -> Left subtree -> Right subtree"""
        if start:
            return [start.value] + self.pre_order_list(start.left) + self.pre_order_list(start.right)
        return []

    # def in_order_print(self, start):
    #     """Left -> root -> right"""
    #     if start:
    #         self.in_order_print(start.left)
    #         print(str(start.value) + '-', end="")
    #         self.in_order_print(start.right)

    def in_order_print(self, start, traversal):
        """Root -> Left subtree -> Right subtree"""
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        """Left subtree -> Right subtree -> root"""
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal


    def depth_first_values(self):
        """Non-recursive first of pre order"""
        result = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print(result)


    def breadth_first(self):
        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def value_exist(self, value):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                return "True"

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return "False"

    def value_exist_recursive(self, start, value):
        if start:
            if start.value == value:
                return True
            else:
                return self.value_exist_recursive(start.left, value) or self.value_exist_recursive(start.right, value)
        return False

    def max_path_sum(self, root):
        if root:
            return root.value + max(self.max_path_sum(root.left), self.max_path_sum(root.right))
        else:
            return 0

    def max_depth_bfs(self):
        queue = deque([self.root])
        max_depth = 0

        while queue:
            for index in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            max_depth += 1
        return max_depth




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("pre order"))
print(tree.print_tree("in order"))
print(tree.print_tree("post order"))

abc_tree = BinaryTree('a')
abc_tree.root.left = Node('b')
abc_tree.root.right = Node('c')
abc_tree.root.left.left = Node('d')
abc_tree.root.left.right = Node('e')
abc_tree.root.right.right = Node('f')

print(abc_tree.print_tree("pre order"))

abc_tree.depth_first_values()
print(abc_tree.pre_order_list(abc_tree.root))
print(abc_tree.breadth_first())
print(abc_tree.value_exist('e'))
print(abc_tree.value_exist_recursive(abc_tree.root, 'f'))
print(tree.sum(tree.root))
print(tree.sum_queue())
print(tree.min_value(tree.root))
print(tree.min_value_queue())


new_tree = BinaryTree(5)
new_tree.root.left = Node(11)
new_tree.root.right = Node(3)
new_tree.root.left.left = Node(4)
new_tree.root.left.right = Node(2)
new_tree.root.right.right = Node(1)

print(new_tree.max_path_sum(new_tree.root))
print(tree.max_depth_bfs())


