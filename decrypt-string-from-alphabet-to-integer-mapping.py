class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Create a result list to collect the resulting characters
        result = []
        # Initialize an index for iteration
        i = 0
        # Iterate over the string
        while i < len(s):
            # Check if the current character and the next two characters form a valid pattern like '10#'
            if i + 2 < len(s) and s[i + 2] == "#":
                # Convert the substring s[i:i+2] to an integer and map it to the corresponding character
                result.append(chr(int(s[i : i + 2]) + ord("j") - 10))
                # Skip the next two characters as they are part of this pattern
                i += 3
            else:
                # Convert the single character s[i] to an integer and map it to the corresponding character
                result.append(chr(int(s[i]) + ord("a") - 1))
                # Move to the next character
                i += 1
        # Join the list of characters to form the resulting string
        return "".join(result)
