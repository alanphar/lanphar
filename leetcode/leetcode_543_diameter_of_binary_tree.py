# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def branch_length(root, diameter):
    if root:
        left_max = branch_length(root.left, diameter)
        right_max = branch_length(root.right, diameter)

        diameter[0] = max(diameter[0], left_max + right_max)

        return max(left_max, right_max) + 1
    else:
        return 0


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root:
            diameter = [0]
            branch_length(root, diameter)
            return diameter[0]
        else:
            return 0
