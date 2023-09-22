# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def getDepth(node):
    depth = 0
    while node:
        depth += 1
        node = node.left
    return depth


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Calculate the depth of the left and right subtrees
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)

        if left_depth == right_depth:
            # If the left and right subtrees have the same depth, the left subtree is a perfect binary tree.
            # The number of nodes in the left subtree can be calculated as 2^left_depth - 1.
            # Add 1 for the root node and recursively count nodes in the right subtree.
            return 2**left_depth + self.countNodes(root.right)
        else:
            # If the left and right subtrees have different depths, the right subtree is a perfect binary tree.
            # The number of nodes in the right subtree can be calculated as 2^right_depth - 1.
            # Add 1 for the root node and recursively count nodes in the left subtree.
            return 2**right_depth + self.countNodes(root.left)
