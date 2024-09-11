class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Get the number of rows (m) and columns (n) in the matrix
        m, n = len(mat), len(mat[0])

        # Variable to store the count of special positions
        special_count = 0

        # Iterate through every position in the matrix
        for i in range(m):
            for j in range(n):
                # If the current position contains a 1
                if mat[i][j] == 1:
                    # Check if it's the only 1 in its row
                    if sum(mat[i]) == 1:
                        # Check if it's the only 1 in its column
                        col_sum = sum(mat[k][j] for k in range(m))
                        if col_sum == 1:
                            # If both conditions are true, increment special_count
                            special_count += 1

        # Return the total number of special positions found
        return special_count
