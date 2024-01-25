# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Initialize an empty set to store the values as we traverse the tree
        seen = set()

        # Helper function to perform in-order traversal and check for the sum
        def inorder_traversal(node):
            # Base case: If the node is None, return False
            if not node:
                return False

            # Check if (k - node.val) is in the set
            if k - node.val in seen:
                return True

            # Add the current node's value to the set
            seen.add(node.val)

            # Recursively traverse the left and right subtrees
            return inorder_traversal(node.left) or inorder_traversal(node.right)

        # Start the traversal from the root
        return inorder_traversal(root)
