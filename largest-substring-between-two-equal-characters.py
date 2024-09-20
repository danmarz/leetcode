class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Dictionary to store the first occurrence of each character
        char_index = {}
        max_length = (
            -1
        )  # Initial maximum length set to -1 for the case of no valid substring

        # Iterate over the string
        for i, char in enumerate(s):
            # If the character has been seen before, calculate the length of the substring
            if char in char_index:
                # Substring length is the difference between the current index and the index of the first occurrence minus 1
                length = i - char_index[char] - 1
                # Update max_length if we find a longer substring
                max_length = max(max_length, length)
            else:
                # Store the index of the first occurrence of the character
                char_index[char] = i

        return max_length
