class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Helper function to check if a string is a palindrome

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        # If the string is empty, it requires 0 steps
        if not s:
            return 0

        # Check if the string itself is a palindrome
        if is_palindrome(s):
            return 1

        # If the string is not a palindrome, it requires 2 steps
        return 2
