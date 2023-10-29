# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = 0

        # Check if the left child of the current node is a leaf (no left or right child).
        if root.left and not root.left.left and not root.left.right:
            left_sum += root.left.val

        # Recursively traverse the left and right subtrees.
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)

        return left_sum
