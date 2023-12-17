# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter
        max_diameter = 0

        # Define a helper function to calculate the depth of the tree
        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update the maximum diameter if a new diameter is found
            nonlocal max_diameter
            max_diameter = max(max_diameter, left_depth + right_depth)

            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)

        # Calculate the depth of the tree
        depth(root)

        return max_diameter
