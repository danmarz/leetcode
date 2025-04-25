class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # Number of columns (same for all rows)
        n = len(grid[0])
        ans = []

        # Iterate over each column index
        for col in range(n):
            max_width = 0  # Store maximum width for current column

            # Iterate through each row to find the max width of the current column
            for row in grid:
                # Convert number to string to include negative sign if present
                width = len(str(row[col]))
                # Update max width if this number is wider
                max_width = max(max_width, width)

            # Append the widest width found for this column
            ans.append(max_width)

        return ans
