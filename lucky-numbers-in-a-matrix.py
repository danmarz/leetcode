class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum element in each row
        min_in_rows = [min(row) for row in matrix]

        # Step 2: Find the maximum element in each column
        max_in_cols = [max(col) for col in zip(*matrix)]

        # Step 3: Find all lucky numbers
        lucky_nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_cols[j]:
                    lucky_nums.append(matrix[i][j])

        return lucky_nums
