class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum


# Senior SWE approach
# if not nums:  # Handle empty array edge case
#     return 0

# max_sum = current_sum = nums[0]

# for i in range(1, len(nums)):
#     current_sum = current_sum + nums[i] if nums[i] > nums[i - 1] else nums[i]
#     max_sum = max(max_sum, current_sum)

# return max_sum
