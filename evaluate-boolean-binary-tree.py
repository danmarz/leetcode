# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:  # Leaf node, False
            return False
        elif root.val == 1:  # Leaf node, True
            return True
        elif root.val == 2:  # OR operation (Short-circuiting added)
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:  # AND operation (Short-circuiting added)
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
