class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize an empty stack to hold characters

        # Iterate through each character in the string
        for char in s:
            # Check if the stack is not empty and the top of the stack forms a bad pair with the current character
            if stack and (
                (stack[-1].islower() and stack[-1].upper() == char)
                or (stack[-1].isupper() and stack[-1].lower() == char)
            ):
                stack.pop()  # Remove the last character from the stack if a bad pair is found
            else:
                stack.append(char)  # Otherwise, add the current character to the stack

        # Join the characters in the stack to form the final "good" string
        return "".join(stack)
