# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        curr_level = 0
        level_lists = []

        while queue:
            curr_level_list = []
            curr_queue_len = len(queue)

            for _ in range(curr_queue_len):
                node = queue.popleft()
                curr_level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_level % 2 != 0:
                curr_level_list.reverse()
            
            curr_level += 1
            level_lists.append(curr_level_list)

        return level_lists