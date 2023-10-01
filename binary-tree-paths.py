# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return

            # Append the current node's value to the path.
            path.append(str(node.val))

            if not node.left and not node.right:
                # If it's a leaf node, add the path to the result list.
                result.append("->".join(path))
            else:
                # Otherwise, continue exploring the left and right subtrees.
                dfs(node.left, path.copy())  # Copy the current path for left subtree.
                dfs(node.right, path.copy())  # Copy the current path for right subtree

        result = []
        dfs(root, [])
        return result
