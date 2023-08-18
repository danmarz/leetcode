# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthCount(root):
            if not root:
                return 0
            left_depth = maxDepthCount(root.left)
            right_depth = maxDepthCount(root.right)
            return max(left_depth, right_depth) + 1

        return maxDepthCount(root)
