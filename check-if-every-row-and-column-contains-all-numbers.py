class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # n = len(matrix[0])

        # # check rows
        # for i in range(1, n + 1):
        #     for j in range(n):
        #         if i not in matrix[j]:
        #             return False

        # # check cols
        # for i in range(1, n + 1):
        #     col = []
        #     j = i - 1
        #     for k in range(n):
        #         col.append(matrix[k][j])
        #     for i in range(1, n + 1):
        #         if i not in col:
        #             return False

        # return True

        # Optimized solution using zip() and sets
        n = len(matrix)
        valid_set = set(range(1, n + 1))  # The set of numbers {1, 2, ..., n}

        for row in matrix:
            if set(row) != valid_set:  # Check if the row contains exactly {1, ..., n}
                return False

        for col in zip(*matrix):  # zip(*matrix) transposes the matrix
            if (
                set(col) != valid_set
            ):  # Check if the column contains exactly {1, ..., n}
                return False

        return True
