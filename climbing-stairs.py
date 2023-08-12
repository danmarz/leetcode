class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Dynamic Programming
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second

        # 2. Dynamic Programming (using a List)
        """
        if n == 1:
            return 1
    
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
    
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
    
        return ways[n]
        """
