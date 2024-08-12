class Solution:
    def maxPower(self, s: str) -> int:
        result = 1
        max_result = 0
        previous_char = ""

        for char in s:
            if char == previous_char:
                result += 1
            else:
                max_result = max(result, max_result)
                result = 1
            previous_char = char

        return max(max_result, result)
