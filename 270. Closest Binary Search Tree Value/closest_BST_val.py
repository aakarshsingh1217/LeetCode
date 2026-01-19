# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        num = None

        def binary_search(node: Optional[TreeNode], target: float):
            if node is None:
                return

            nonlocal diff
            nonlocal num

            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                num = node.val
            if abs(node.val - target) == diff:
                num = min(num, node.val)

            if target < node.val:
                binary_search(node.left, target)
            if target > node.val:
                binary_search(node.right, target)

        binary_search(root, target)

        return num