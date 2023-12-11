# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        values = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            values.append(root.val)

        traverse(root)

        values = sorted(values)

        minimum = values[1] - values[0]

        for i in range(1, len(values)):
            if values[i] - values[i - 1] < minimum:
                minimum = values[i] - values[i - 1]

        return minimum
        """

        # Elegant approach:

        def inorder_traversal(node):
            nonlocal prev, min_diff

            if node is None:
                return

            # Visit left subtree
            inorder_traversal(node.left)

            # Calculate the absolute difference
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)

            # Update prev for the next comparison
            prev = node.val

            # Visit right subtree
            inorder_traversal(node.right)

        # Initialize variables
        prev = None
        min_diff = float("inf")  # Initialize with a large value

        # Start the traversal from the root
        inorder_traversal(root)

        return min_diff
