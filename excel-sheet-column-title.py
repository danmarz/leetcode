class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            # Minus 1 to handle 1-based indexing in Excel
            columnNumber -= 1

            # Calculate the remainder when divided by 26 (0-25 corresponds to A-Z).
            remainder = columnNumber % 26

            # Append the corresponding letter to the left of the result string. ord('A') is 65
            result = chr(65 + remainder) + result

            # Floor divide columnNumber by 26.
            columnNumber //= 26

        return result
