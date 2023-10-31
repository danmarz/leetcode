class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}  # Dictionary to store character frequencies.

        # Count the frequency of each character in the string.
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        length = 0
        has_odd = False

        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True

        # If there's at least one character with an odd count, add one more to the length.
        if has_odd:
            length += 1

        return length
