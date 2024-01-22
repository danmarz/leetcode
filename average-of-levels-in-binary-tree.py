# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Check if the tree is empty
        if not root:
            return []

        # List to store average values for each level
        result = []
        # Queue for level order traversal
        queue = deque([root])

        # Perform level order traversal
        while queue:
            # Get the size of the current level
            level_size = len(queue)
            # Variable to store the sum of node values in the current level
            level_sum = 0

            # Process nodes in the current level
            for _ in range(level_size):
                # Dequeue a node
                node = queue.popleft()
                # Add its value to the sum
                level_sum += node.val

                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate and append the average value for the current level
            result.append(level_sum / level_size)

        return result
