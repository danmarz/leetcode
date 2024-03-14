class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_area = sum(max(row) for row in grid)  # Projection onto xy-plane
        yz_area = sum(
            max(grid[i][j] for i in range(n)) for j in range(n)
        )  # Projection onto yz-plane
        zx_area = sum(
            1 for i in range(n) for j in range(n) if grid[i][j] > 0
        )  # Projection onto zx-plane
        return xy_area + yz_area + zx_area
