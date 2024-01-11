class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Check if the operations list is empty
        if not ops:
            # If no operations, the entire matrix is filled
            return m * n

        # Initialize minimum row and column values to infinity
        min_row = float("inf")
        min_col = float("inf")

        # Iterate through each operation
        for op in ops:
            # Update minimum row value
            min_row = min(min_row, op[0])
            # Update minimum column value
            min_col = min(min_col, op[1])

        # Return the product of minimum row and column values
        return min_row * min_col
