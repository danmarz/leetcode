class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # For each land cell, count its perimeter edges
                    perimeter += 4  # Start with assuming all edges are present

                    # Check adjacent cells (up, down, left, right) and subtract connected edges
                    if i > 0 and grid[i - 1][j] == 1:  # Check above cell
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:  # Check left cell
                        perimeter -= 2

        return perimeter
