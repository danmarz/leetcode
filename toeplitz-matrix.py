class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])

        # Check all the diagonals starting from the first row
        for i in range(m):
            for j in range(n):
                # For each cell (i, j), check if its value matches the value of the top-left neighbor
                if i > 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                    # If not, return False
                    return False
        # If all diagonals have the same elements, return True
        return True
