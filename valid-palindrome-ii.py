class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            # Helper function to check if substring s[i:j+1] is a palindrome
            return all(s[k] == s[j - k + i] for k in range(i, j))

        # Iterate through the string
        for i in range(len(s) // 2):
            # If characters at corresponding positions are different
            if s[i] != s[~i]:
                # Check if deleting either of them makes the rest a palindrome
                j = len(s) - 1 - i
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)

        # If we didn't find any non-matching pairs, it's already a palindrome or can be made by deleting at most one character
        return True
