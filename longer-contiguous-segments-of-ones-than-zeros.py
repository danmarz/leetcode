class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # Initialize variables to track maximum lengths of contiguous 1's and 0's
        max_ones = max_zeroes = 0
        current_ones = current_zeroes = 0

        for char in s:
            if char == "1":
                current_ones += 1  # Increment count of 1's
                current_zeroes = 0  # Reset count of 0's
                max_ones = max(max_ones, current_ones)  # Update max for 1's
            else:  # char == '0'
                current_zeroes += 1  # Increment count of 0's
                current_ones = 0  # Reset count of 1's
                max_zeroes = max(max_zeroes, current_zeroes)  # Update max for 0's

        # Compare maximum lengths of contiguous 1's and 0's
        return max_ones > max_zeroes
