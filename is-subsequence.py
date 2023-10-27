class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Initialize pointers for strings s and t.

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move the s pointer if there's a match.
            j += 1  # Always move the t pointer.

        return i == len(s)  # If the s pointer reached the end, s is a subsequence of t.
