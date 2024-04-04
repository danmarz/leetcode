class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()

        # Iterate through the array from the end
        for i in range(len(nums) - 1, 1, -1):
            # Check if the sum of the two smaller lengths is greater than the largest length
            if nums[i - 2] + nums[i - 1] > nums[i]:
                # If it is, return the perimeter
                return nums[i - 2] + nums[i - 1] + nums[i]
        # If no valid triangle is found, return 0
        return 0
