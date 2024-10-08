# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def verify(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return verify(p.left, q.left) and verify(p.right, q.right)

        return verify(p, q)

    ## Alternative solution: Convert both trees to string and equate them
    """
        return str(p) == str(q)
    """
