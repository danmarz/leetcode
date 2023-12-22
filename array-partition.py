class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array to group adjacent elements
        max_sum = 0

        # Pair the elements by selecting alternate elements
        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum
