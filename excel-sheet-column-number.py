class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            position_value = ord(char) - ord("A") + 1  # ord('A') == 65
            result = result * 26 + position_value

        return result
