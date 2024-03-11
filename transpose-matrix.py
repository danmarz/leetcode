class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the original matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a new matrix to store the transposed matrix
        transposed = [[0] * rows for _ in range(cols)]

        # Iterate through each element in the original matrix
        for i in range(rows):
            for j in range(cols):
                # Place the element at its corresponding position in the transposed matrix
                transposed[j][i] = matrix[i][j]

        return transposed
