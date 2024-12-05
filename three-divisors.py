class Solution:
    def isThree(self, n: int) -> bool:
        # if n == 1 or n == 2:
        #     return False

        # divisors = 0
        # for i in range(2, n):
        #     if n / i == float(n // i):
        #         divisors += 1
        # return divisors == 1

        # # Initialize a counter for divisors
        # divisor_count = 0

        # # Check every number from 1 to n
        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         divisor_count += 1

        # # Return True if exactly three divisors are found
        # return divisor_count == 3

        # Optimized Solution: Efficient, leveraging mathematical properties: O(sqrt(n)) due to prime check
        # Helper function to check if a number is prime
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Check if n is a perfect square
        root = int(n**0.5)
        if root * root != n:
            return False

        # Check if the square root is prime
        return is_prime(root)
