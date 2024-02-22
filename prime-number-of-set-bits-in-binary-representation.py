class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Function to check if a number is prime
        def is_prime(n):
            # 0 and 1 are not prime numbers
            if n < 2:
                return False
            # Check for divisibility by numbers from 2 to sqrt(n)
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # Initialize a variable to count the prime set bits numbers
        count = 0

        # Iterate through the range [left, right] (inclusive)
        for num in range(left, right + 1):
            # Count the number of set bits in the binary representation of num
            set_bits = bin(num).count("1")
            # Check if the count of set bits is a prime number
            if is_prime(set_bits):
                # If it's prime, increment the count
                count += 1

        # Return the count of numbers with a prime number of set bits
        return count
