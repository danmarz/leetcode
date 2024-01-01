# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:  # If the root is None, return False
            return False

        # Helper function to check if two trees are identical
        def is_identical(s, t):
            if not s and not t:  # Both nodes are None
                return True
            if not s or not t:  # One node is None but not both
                return False
            return (
                s.val == t.val
                and is_identical(s.left, t.left)
                and is_identical(s.right, t.right)
            )

        # Check if the current root is identical to the subRoot
        if is_identical(root, subRoot):
            return True

        # Recursively check if the subtree exists in the left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
