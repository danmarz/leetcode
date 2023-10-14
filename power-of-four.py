class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """Using isqrt
        return n > 0 and not(n & (n-1)) and isqrt(n) * isqrt(n) == n
        """

        """ Using bitwise operators
        return n and not (n & (n - 1)) and (n & 0x55555555)

        # which can also be written as

        return n > 0 and not(n & (n - 1)) and n & 1431655765 == n
        """

        """ Using log function
        return n > 0 and log(n,4).is_integer()
        """

        """ O(1) solution
        if n > 0:
            if 4**round(math.log(n,4),0) == n:
                return True
        """

        # Brute force solution
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False

        while n > 4:
            n /= 4

        return n == 4
