class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n <= 1:
            return False

        divisors_sum = 1  # Start with 1 because it's a divisor for all numbers

        # Find divisors and sum them up
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if (
                    i != n // i
                ):  # Avoid adding the same divisor twice for perfect squares
                    divisors_sum += n // i
        return divisors_sum == n
