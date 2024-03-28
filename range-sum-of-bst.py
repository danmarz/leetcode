# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # Calculate the sum of values within the range [low, high]
        sum_val = root.val if low <= root.val <= high else 0

        # Recursively search both left and right subtrees and add their results directly
        sum_val += self.rangeSumBST(root.left, low, high) + self.rangeSumBST(
            root.right, low, high
        )

        return sum_val
