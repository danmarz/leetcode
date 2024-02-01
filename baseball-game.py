class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Initialize an empty list to keep track of the valid scores
        stack = []

        # Iterate through each operation
        for op in operations:
            if op == "C":
                # If the operation is 'C', pop the last valid score from the stack
                stack.pop()
            elif op == "D":
                # If the operation is 'D', double the last valid score and add to the stack
                stack.append(2 * stack[-1])
            elif op == "+":
                # If the operation is '+', add the sum of the last two valid scores to the stack
                stack.append(stack[-1] + stack[-2])
            else:
                # If the operation is an integer, add it to the stack
                stack.append(int(op))

        # Return the sum of all valid scores on the record
        return sum(stack)
