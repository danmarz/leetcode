# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = [(root, root.val)]
        
        while queue:
            node, runningSum = queue.pop(0)
            if not node.left and not node.right and runningSum == targetSum:
                return True
            if node.left:
                queue.append((node.left, runningSum + node.left.val))
            if node.right:
                queue.append((node.right, runningSum + node.right.val))
        return False
"""

# Solution 2


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: If node is None, return False
        if not root:
            return False

        # Subtract the value of the current node from target sum
        targetSum -= root.val

        # If current node is a leaf, check if target sum is 0
        if not root.left and not root.right:
            return targetSum == 0

        # Recursively call for left and right children
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )
