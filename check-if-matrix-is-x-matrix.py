class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)  # No need to get len(grid[0]), it's a square matrix

        for i in range(n):
            for j in range(n):  # Iterate correctly within the n x n grid
                if i == j or j == (n - i - 1):  # Check diagonal elements
                    if grid[i][j] == 0:  # Diagonal elements must be nonzero
                        return False
                else:  # Non-diagonal elements
                    if grid[i][j] != 0:  # Must be zero
                        return False

        return True
