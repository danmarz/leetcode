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

        # One line alternative
        # return Counter(s) == Counter(t)

        """
        Overall, using the Counter class is a recommended and efficient way to check if two strings are anagrams. This approach has the following advantages:

        - It's concise and easy to read, making the code more maintainable.
        - It leverages Python's built-in data structures and operations, which are optimized for efficiency.
        - It runs in O(n) time complexity, where n is the length of the strings, as it iterates through both strings once to create the character count dictionaries and then compares them.
        - It runs in O(1) space complexity, as the size of the character count dictionaries is bounded by the number of unique characters in the strings.
        """
