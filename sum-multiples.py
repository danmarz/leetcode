class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_divisible_by(k, n):
            # m = number of multiples of k up to n
            m = n // k
            # sum of arithmetic progression: k + 2k + ... + mk = k * (1 + 2 + ... + m)
            return k * m * (m + 1) // 2

        # Inclusion-Exclusion Principle
        total = (
            sum_divisible_by(3, n)
            + sum_divisible_by(5, n)
            + sum_divisible_by(7, n)
            - sum_divisible_by(3 * 5, n)
            - sum_divisible_by(3 * 7, n)
            - sum_divisible_by(5 * 7, n)
            + sum_divisible_by(3 * 5 * 7, n)
        )
        return total
