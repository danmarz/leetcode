class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_length = 0
        i = 0

        while i < len(s):
            # Count zeros in current group
            count_zeros = 0
            while i < len(s) and s[i] == "0":
                count_zeros += 1
                i += 1

            # Count ones immediately after the zeros
            count_ones = 0
            while i < len(s) and s[i] == "1":
                count_ones += 1
                i += 1

            # Update max balanced substring length
            max_length = max(max_length, 2 * min(count_zeros, count_ones))

        return max_length
