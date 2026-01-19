# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], ans: int):
            if node is None:
                return float("inf")
            if node.left is None and node.right is None:
                return ans + 1

            left = dfs(node.left, ans + 1)
            right = dfs(node.right, ans + 1)

            return min(left, right)

        if root is None:
            return 0

        return dfs(root, 0)
        