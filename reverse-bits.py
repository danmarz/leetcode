class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1  # Shift the result to the left by 1 bit
            result |= n & 1  # Add the rightmost bit of n to the result
            n >>= 1  # Shift n to the right by 1 bit
        return result
