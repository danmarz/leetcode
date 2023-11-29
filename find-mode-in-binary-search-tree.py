# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the tree is empty
        if not root:
            return []

        # Dictionary to store frequencies of elements in the BST
        freq_map = {}
        # List to store the maximum frequency encountered during traversal
        max_freq = [0]

        # Helper function for in-order traversal
        def inorder(node):
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Update frequency map for the current node's value
            freq_map[node.val] = freq_map.get(node.val, 0) + 1
            # Update the maximum frequency encountered
            max_freq[0] = max(max_freq[0], freq_map[node.val])

            # Traverse right subtree
            inorder(node.right)

        # Perform in-order traversal to populate frequency map and find max frequency
        inorder(root)

        # Collect elements with frequencies equal to max frequency as modes
        modes = [key for key, value in freq_map.items() if value == max_freq[0]]
        return modes
