class Solution:
    def fib(self, n: int, memo={}) -> int:
        # optimized approach, using memoization
        if n in memo:
            return memo[n]
        if n <= 1:
            return n

        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        return memo[n]

        # iterative solution

    """   
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        prev_1, prev_2 = 0, 1

        for i in range(2, n + 1):
            current = prev_1 + prev_2
            prev_1, prev_2 = prev_2, current

        return prev_2
    """
