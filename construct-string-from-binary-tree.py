# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """ "
        # Helper function to convert a tree node to a string
         def nodeToStr(node):
             if not node:
                 return ""
             return str(node.val) + "(" + nodeToStr(node.left) + ")" + "(" + nodeToStr(node.right) + ")"
         # Call the helper function on the root node
         return nodeToStr(root)
        """
        if not root:
            return ""

        result = str(root.val)

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if left_str or right_str:
            result += f"({left_str})"

        if right_str:
            result += f"({right_str})"

        return result
