class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize row and column counters
        row_count = [0] * m
        col_count = [0] * n

        # Apply increments as per the indices
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        print(row_count)
        print(col_count)
        # Calculate the number of odd-valued cells
        odd_count = 0
        for i in range(m):
            for j in range(n):
                print(row_count[i], col_count[j])
                if (row_count[i] + col_count[j]) % 2 == 1:
                    odd_count += 1

        return odd_count
