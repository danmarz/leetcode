class Solution:
    def countTriples(self, n: int) -> int:
        # Bruteforce approach
        nums = [_ for _ in range(1, n + 1)]
        count = 0
        for a in nums:
            for b in nums:
                c = sqrt(a**2 + b**2)
                if c in nums:
                    count += 1
        return count

        # # Optimized approach:
        # count = 0
        # for a in range(1, n + 1):
        #     for b in range(a, n + 1):  # Avoid symmetry by starting b from a
        #         c_squared = a**2 + b**2
        #         c = int(math.sqrt(c_squared))
        #         if c**2 == c_squared and c <= n:
        #             count += 1
        # return count * 2  # Multiply by 2 to account for (a, b, c) and (b, a, c)
