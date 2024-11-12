class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum_n = 0

        while n > 0:
            sum_n = sum_n + n % k
            n = n // k

        return sum_n

        # # String manipulation alternative:
        # # Convert `n` to base `k` and store as a string
        # n_base_k = ""
        # while n > 0:
        #     n_base_k = str(n % k) + n_base_k  # Build the string from right to left
        #     n //= k

        # # Sum up the digits in the base-k representation
        # return sum(int(digit) for digit in n_base_k)
