# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def calculateTiltAndSum(node):
            nonlocal total_tilt

            if not node:
                return 0

            left_sum = calculateTiltAndSum(node.left)
            right_sum = calculateTiltAndSum(node.right)

            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return left_sum + right_sum + node.val

        total_tilt = 0
        calculateTiltAndSum(root)

        return total_tilt
