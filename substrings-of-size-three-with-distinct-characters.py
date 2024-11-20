class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            # Extract a substring of length 3
            substring = s[i : i + 3]
            # Check if all characters in the substring are unique
            if len(set(substring)) == 3:
                count += 1
        return count
