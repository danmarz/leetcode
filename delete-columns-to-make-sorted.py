class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Initialize a variable to keep track of the number of columns to delete
        count = 0

        # Iterate over each column of the grid
        for col in zip(*strs):
            # Check if the column is not sorted lexicographically
            if sorted(col) != list(col):
                # Increment the count of columns to delete
                count += 1

        # Return the number of columns to delete
        return count
