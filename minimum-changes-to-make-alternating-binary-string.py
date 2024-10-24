class Solution:
    def minOperations(self, s: str) -> int:
        mismatches_start_with_0 = mismatches_start_with_1 = 0

        # Loop through the string and count mismatches for both patterns
        for i, char in enumerate(s):
            if char != ("0" if i % 2 == 0 else "1"):
                mismatches_start_with_0 += 1
            if char != ("1" if i % 2 == 0 else "0"):
                mismatches_start_with_1 += 1

        return min(mismatches_start_with_0, mismatches_start_with_1)
