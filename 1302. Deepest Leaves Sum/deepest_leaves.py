# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 0

        while queue:
            curr_ans = 0
            queue_len = len(queue)

            for _ in range(queue_len):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    curr_ans += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans = curr_ans

        return ans