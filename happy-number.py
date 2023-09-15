class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # Create a set to keep track of seen numbers

        while n != 1:
            n = sum(
                int(digit) ** 2 for digit in str(n)
            )  # Calculate the sum of squares of digits
            if n in seen:
                return False  # If a number is repeated, it's in a cycle and not a happy number
            seen.add(n)  # Add the current number to the set of seen numbers

        return True  # If n eventually becomes 1, it's a happy number
