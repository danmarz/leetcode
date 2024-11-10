class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                ops += (nums[i - 1] + 1) - nums[i]
                nums[i] = nums[i - 1] + 1  # Update to ensure strictly increasing
        return ops
