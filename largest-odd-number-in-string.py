class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1

        while i >= 0:
            if int(num[i]) % 2 == 1:
                return num[: i + 1]
            i -= 1

        return ""

        # More compact:
        for i in range(len(num) - 1, -1, -1):  # Iterate from the end
            if int(num[i]) % 2 == 1:  # Check if the digit is odd
                return num[: i + 1]  # Return substring from start to this position
        return ""  # No odd digit found
