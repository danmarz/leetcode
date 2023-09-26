class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Relying on the fact that the binary representation of a power of two contains only one '1' bit followed by zeros. Counting the number of '1' bits in a binary string gives us the ability to determine whether the number is a power of two or not.

        return bin(n).count("1") == 1 if n > 0 else False


# The same logic, but instead of bin().count() we use bitwise AND operation: result of the bitwise AND operation between a number and its complement will always be 0. If the result is not 0, then the number is not a power of 2 because it has at least one bit set to '1' that is not the least significant bit.

"""
        return n & (n - 1) == 0 and n > 0
"""

# And one could say brute force iterative solution:

"""
        while n:
            if n == 1:
                return True
            elif n % 2 == 0:
                n /= 2
            else:
                return False
"""

# Also possible using recursion instead of a loop:

"""
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        
        return False
"""
