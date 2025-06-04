def path_sums(root, targetSum, path_sums_list, path_list):
    if not root:
        return

    path_list.append(root.val)
    if not root.left and not root.right:
        if targetSum == root.val:
            path_sums_list.append(list(path_list))
    
    path_sums(root.left, targetSum - root.val, path_sums_list, path_list)
    path_sums(root.right, targetSum - root.val, path_sums_list, path_list)

    path_list.pop()


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path_sums_list = []

        path_sums(root, targetSum, path_sums_list, [])
        return path_sums_list
