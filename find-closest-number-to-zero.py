class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # # Bruteforce it
        # for n in range(100000 + 1):
        #     if n in nums:
        #         return n
        #     elif -n in nums:
        #         return -n

        # Elegant
        min_value = nums[0]
        for n in nums:
            if abs(n) < abs(min_value):
                min_value = n

        if min_value < 0 and abs(min_value) in nums:
            return abs(min_value)
        else:
            return min_value
