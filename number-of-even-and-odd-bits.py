class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # str_bin_n = str(bin(n)[2:])[::-1]
        # odd = 0
        # even = 0

        # for i in range(len(str_bin_n)):
        #     if str_bin_n[i] == '1':
        #         if i % 2 == 0:
        #             even += 1
        #         else:
        #             odd += 1

        # return [even, odd]

        # Bitwise shift approach:
        even = odd = 0  # Initialize counters for even and odd positions
        idx = 0  # Start indexing bits from 0 (rightmost)

        while n > 0:
            if n & 1:  # Check if current bit is set (1)
                if idx % 2 == 0:  # Even index
                    even += 1
                else:  # Odd index
                    odd += 1
            n >>= 1  # Shift right to check next bit
            idx += 1  # Increment index

        return [even, odd]
