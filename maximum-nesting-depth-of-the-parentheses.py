class Solution:
    def maxDepth(self, s: str) -> int:
        # Initialize a variable to keep track of the current depth
        current_depth = 0

        # Initialize a variable to store the maximum depth encountered
        max_depth = 0

        # Loop through each character in the string
        for char in s:
            # If the character is an opening parenthesis, increase the current depth
            if char == "(":
                current_depth += 1
                # Update the max depth if the current depth exceeds the previous max depth
                max_depth = max(max_depth, current_depth)

            # If the character is a closing parenthesis, decrease the current depth
            elif char == ")":
                current_depth -= 1

        # After the loop, return the maximum depth found
        return max_depth
