class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        min_n = nums[0]
        max_n = nums[0]

        for num in nums:
            if num > max_n:
                max_n = num
            elif num < min_n:
                min_n = num

        return gcd(min_n, max_n)

        # # Alternative using math library:
        # return math.gcd(min(nums), max(nums))
