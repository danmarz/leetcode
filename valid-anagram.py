class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of s and t are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Initialize a dictionary to count character occurrences in s.
        char_count = {}

        # Count occurrences of characters in s.
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Compare character occurrences in t with those in s.
        for char in t:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                # If a character in t is not found in s or has already been used up,
                # t cannot be an anagram of s.
                return False

        return True
