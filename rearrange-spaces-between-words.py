class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Count total number of spaces
        total_spaces = text.count(" ")

        # Split the text into words
        words = text.split()
        num_words = len(words)

        # If there's only one word, all spaces go at the end
        if num_words == 1:
            return words[0] + " " * total_spaces

        # Calculate spaces between words and extra spaces
        spaces_between = total_spaces // (num_words - 1)
        extra_spaces = total_spaces % (num_words - 1)

        # Reconstruct the text
        equal_space = " " * spaces_between
        result = equal_space.join(words) + " " * extra_spaces
        return result
