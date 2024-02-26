# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to store the minimum difference
        min_diff = float("inf")
        # Initialize a variable to store the previously visited value
        prev_val = None

        # Define a helper function to perform in-order traversal
        def inorder_traversal(node):
            nonlocal min_diff, prev_val
            if node is None:
                return
            # Traverse left subtree
            inorder_traversal(node.left)
            # Update min_diff if prev_val is not None
            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
            # Update prev_val
            prev_val = node.val
            # Traverse right subtree
            inorder_traversal(node.right)

        # Start in-order traversal from the root
        inorder_traversal(root)

        # Return the minimum difference found
        return min_diff
