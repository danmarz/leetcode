class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = "abcdefgh"

        if letters.index(coordinates[0]) % 2 == 0:
            if int(coordinates[1]) % 2 != 0:
                return False
            return True
        if letters.index(coordinates[0]) % 2 == 1:
            if int(coordinates[1]) % 2 == 0:
                return False
            return True

        # # More concise approach:
        # letters = "abcdefgh"
        # col_index = letters.index(coordinates[0])  # index of the letter
        # row_index = int(coordinates[1])  # numeric part of the coordinate

        # # Calculate whether the square is white by checking if the sum of indices is odd
        # return (col_index + row_index) % 2 != 0
