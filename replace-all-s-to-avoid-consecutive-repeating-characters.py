class Solution:
    def modifyString(self, s: str) -> str:
        # Convert the input string to a list for easy modification
        s = list(s)

        # Iterate over every character in the string
        for i in range(len(s)):
            # Check if the current character is a '?'
            if s[i] == "?":
                # Try all lowercase letters to replace '?'
                for char in "abc":
                    # Check if the current character doesn't match the previous and next one
                    # This ensures no consecutive repeating characters
                    if (i == 0 or s[i - 1] != char) and (
                        i == len(s) - 1 or s[i + 1] != char
                    ):
                        s[i] = char  # Replace '?' with the chosen character
                        break  # Move to the next character after successful replacement

        # Join the list back into a string and return it
        return "".join(s)
