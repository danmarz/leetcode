# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Helper function for DFS traversal
        def dfs(node, parent, depth, target, info):
            if not node:
                return
            if node.val == target:
                info["parent"] = parent
                info["depth"] = depth
                return
            dfs(node.left, node, depth + 1, target, info)
            dfs(node.right, node, depth + 1, target, info)

        # Dictionary to store depth and parent information for each node
        node_info = {}

        # Perform DFS to find depth and parent of node with value x
        dfs(root, None, 0, x, node_info)
        x_depth, x_parent = node_info["depth"], node_info["parent"]

        # Perform DFS to find depth and parent of node with value y
        dfs(root, None, 0, y, node_info)
        y_depth, y_parent = node_info["depth"], node_info["parent"]

        # Check if nodes have the same depth and different parents
        return x_depth == y_depth and x_parent != y_parent
