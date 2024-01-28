# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Initialize a set to store unique node values
        unique_values = set()

        # DFS traversal to collect unique node values
        def dfs(node):
            if node:
                unique_values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        # Perform DFS traversal starting from the root
        dfs(root)

        # If there are fewer than 2 unique values, no second minimum exists
        if len(unique_values) < 2:
            return -1

        # Find and return the second minimum value
        unique_values.remove(min(unique_values))
        return min(unique_values)
