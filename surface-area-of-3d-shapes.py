class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0

        # Iterate through each cell in the grid
        for i in range(n):
            for j in range(n):
                # If the current cell has cubes stacked on it
                if grid[i][j] > 0:
                    # Calculate the surface area of the current cube
                    area = 4 * grid[i][j] + 2

                    # Subtract the area of adjacent faces that are glued together
                    if i > 0:
                        area -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j > 0:
                        area -= min(grid[i][j], grid[i][j - 1]) * 2

                    # Add the surface area of the current cube to the total area
                    total_area += area

        return total_area
