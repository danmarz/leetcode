class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the maximum element in the array
        largest = max(nums)

        # Check if the maximum element is at least twice as much as every other number
        for num in nums:
            if num != largest and 2 * num > largest:
                return -1

        # Return the index of the largest element
        return nums.index(largest)
