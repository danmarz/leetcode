class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # Initialize variables to store the number of lines and the width of the last line
        lines = 1
        width = 0

        # Iterate over each character in the string
        for char in s:
            # Get the width of the current character
            char_width = widths[ord(char) - ord("a")]
            # Add the width of the current character to the total width
            width += char_width
            # If the total width exceeds 100, start a new line
            if width > 100:
                lines += 1
                # Reset the width to the width of the current character
                width = char_width

        # Return the number of lines and the width of the last line
        return [lines, width]
