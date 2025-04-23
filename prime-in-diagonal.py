class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            # Return False for numbers <= 1
            if n <= 1:
                return False
            # Check divisibility up to square root of n
            for i in range(2, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        max_prime = 0
        n = len(nums)  # Number of rows
        m = len(nums[0])  # Number of columns

        for i in range(min(n, m)):
            # Check main diagonal element
            if is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            # Check anti-diagonal element
            if is_prime(nums[i][m - i - 1]):
                max_prime = max(max_prime, nums[i][m - i - 1])

        return max_prime
