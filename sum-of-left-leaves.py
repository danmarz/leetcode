# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # initialize an empty queue
        queue = []
        # add the root node to the queue with a flag ('root' - root, 'l' - left, 'r' - right)
        queue.append((root, "root"))
        # initialize the answer
        ans = 0
        # if the root is empty, return 0
        if not root:
            return 0
        # while the queue is not empty
        while len(queue) > 0:
            # get the size of the queue
            size = len(queue)
            # pop the node from the queue
            node, flag = queue.pop(0)
            # check if the node has a left child
            if node.left:
                # append the left child to the queue with a flag
                queue.append((node.left, "l"))
            # check if the node has a right child
            if node.right:
                # append the right child to the queue with a flag
                queue.append((node.right, "r"))
            # check if the node is a left leaf
            if not node.left and not node.right and flag == "l":
                # add its value to the answer
                ans += node.val
        # return the answer
        return ans

        """ 
        # Recursive approach
        if not root:
            return 0
        
        left_sum = 0

        # Check if the left child of the current node is a leaf (no left or right child).
        if root.left and not root.left.left and not root.left.right:
            left_sum += root.left.val

        # Recursively traverse the left and right subtrees.
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)

        return left_sum
        """
