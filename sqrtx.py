class Solution:
    def mySqrt(self, x: int) -> int:
        # Solution 1: brute force
        ans = 0

        for i in range(x + 1):
            if i * i > x:
                ans = i - 1
                break
            elif i * i == x:
                ans = i
                break

        return ans

        # Solution 2: Newton's method (binary search)
        l, r = 0, x

        while l <= r:
            mid = l + (r - l) // 2
            if mid**2 == x:
                return mid
            if mid**2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

        # Solution 3: math.sqrt()  (not allowed)
        import math

        return int(math.sqrt(x))
