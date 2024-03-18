class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        # Iterate through the array to check if it is monotone increasing
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
                break

        # Iterate through the array to check if it is monotone decreasing
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
                break

        # Return True if the array is monotone increasing or monotone decreasing
        return increasing or decreasing
