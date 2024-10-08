"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        max_child_depth = 0

        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))
            print(child.val)
            print(max_child_depth)

        return 1 + max_child_depth
