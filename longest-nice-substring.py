class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Base case: if the string is empty or has just one character, it cannot be nice.
        if len(s) < 2:
            return ""

        # Check each character in the string.
        for i, char in enumerate(s):
            # If both uppercase and lowercase of the character aren't present, split around it.
            if char.lower() not in s or char.upper() not in s:
                # Recursively check left and right substrings around the character.
                left_substring = self.longestNiceSubstring(s[:i])
                right_substring = self.longestNiceSubstring(s[i + 1 :])

                # Return the longest of the two substrings (or the left if they are of equal length).
                return (
                    left_substring
                    if len(left_substring) >= len(right_substring)
                    else right_substring
                )

        # If the entire string is nice, return it.
        return s
