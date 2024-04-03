# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function to perform DFS traversal
        def dfs(node, val):
            # Base case: If the node is None, return True
            if not node:
                return True
            # If the value of the current node is not equal to the root value, return False
            if node.val != val:
                return False
            # Recursively check the left and right subtrees
            return dfs(node.left, val) and dfs(node.right, val)

        # Call the helper function starting from the root node with the value of the root node
        return dfs(root, root.val)
