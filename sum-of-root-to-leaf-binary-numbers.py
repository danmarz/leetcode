# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            # Update the current binary number by left-shifting and adding the current node's value
            current_sum = (current_sum << 1) | node.val
            # If the current node is a leaf, return the current binary number
            if not node.left and not node.right:
                return current_sum
            # Otherwise, recursively calculate the sum for left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        # Start the depth-first traversal from the root with an initial sum of 0
        return dfs(root, 0)
