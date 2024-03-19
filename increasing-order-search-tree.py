# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(root, nodes):
            if root is None:
                return
            inorderTraversal(root.left, nodes)
            nodes.append(root)
            inorderTraversal(root.right, nodes)

        nodes = []
        # Perform in-order traversal to collect nodes
        inorderTraversal(root, nodes)

        # Rebuild the tree
        new_root = current = TreeNode()
        for node in nodes:
            node.left = None
            current.right = node
            current = node
        return new_root.right
