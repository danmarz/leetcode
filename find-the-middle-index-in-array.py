class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for middle in range(len(nums)):
            right_sum = total_sum - left_sum - nums[middle]
            if left_sum == right_sum:
                return middle
            left_sum += nums[middle]

        return -1
