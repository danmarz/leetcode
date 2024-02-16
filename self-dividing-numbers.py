class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Define a function to check if a number is self-dividing
        def isSelfDividing(num):
            # Convert the number to a string to iterate over its digits
            for digit in str(num):
                # Convert the digit back to an integer
                digit = int(digit)
                # Check if the digit is zero or if the number is not divisible by the digit
                if digit == 0 or num % digit != 0:
                    # If either condition is met, return False
                    return False
            # If all digits are checked and the number is self-dividing, return True
            return True

        # Initialize a list to store the self-dividing numbers
        result = []
        # Iterate through the range from left to right (inclusive)
        for num in range(left, right + 1):
            # Check if the current number is self-dividing
            if isSelfDividing(num):
                # If it is, append it to the result list
                result.append(num)
        # Return the list of self-dividing numbers
        return result
