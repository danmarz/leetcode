class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a variable to count the '1' bits
        count = 0

        # Loop until n becomes 0
        while n > 0:
            # Use bitwise AND to check the least significant bit
            # If it's 1, increment the count
            count += n & 1
            # Right shift n to check the next bit
            n >>= 1

        return count
