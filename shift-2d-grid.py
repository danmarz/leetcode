class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n

        # Flatten the grid into a single list
        flat_list = [grid[i][j] for i in range(m) for j in range(n)]

        # Compute the new index for each element after k shifts
        new_list = [0] * total_elements
        for i in range(total_elements):
            new_index = (i + k) % total_elements
            new_list[new_index] = flat_list[i]

        # Convert the 1D list back into a 2D grid
        new_grid = [[0] * n for _ in range(m)]
        for i in range(total_elements):
            row, col = divmod(i, n)
            new_grid[row][col] = new_list[i]

        return new_grid
