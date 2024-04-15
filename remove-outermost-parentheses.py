class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        open_count = 0
        start = 0
        for i, char in enumerate(s):
            if char == "(":
                open_count += 1
            else:
                open_count -= 1
            # If open_count becomes 0, it means we found the end of a primitive substring
            if open_count == 0:
                # Remove outer parentheses and append the primitive substring to result
                result += s[start + 1 : i]
                start = i + 1  # Update the start index for the next primitive substring
        return result
