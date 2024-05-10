class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Sieve of Eratosthenes to find primes up to n
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        # Count prime indices
        prime_indices = [i for i in range(1, n + 1) if primes[i]]

        # Count non-prime indices
        non_prime_indices = [i for i in range(1, n + 1) if not primes[i]]

        # Compute factorial modulo MOD
        def factorial(x):
            result = 1
            for i in range(1, x + 1):
                result = (result * i) % MOD
            return result

        # Compute total permutations modulo MOD
        total_permutations = (
            factorial(len(prime_indices)) * factorial(len(non_prime_indices))
        ) % MOD

        return total_permutations
