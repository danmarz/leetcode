class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # Stack to store characters
        for char in s:
            # Check if the stack is not empty and the current character is equal to the top character of the stack
            if stack and char == stack[-1]:
                stack.pop()  # Remove the top character from the stack
            else:
                stack.append(char)  # Push the current character onto the stack
        # Convert the stack to a string and return it
        return "".join(stack)
