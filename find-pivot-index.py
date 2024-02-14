class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate the total sum of all elements in the array
        total_sum = sum(nums)
        # Initialize the left sum to 0
        left_sum = 0
        # Iterate through the array along with the index
        for i, num in enumerate(nums):
            # Check if the left sum is equal to the total sum
            # minus the left sum and the current element
            if left_sum == total_sum - left_sum - num:
                # If it is, return the current index as the pivot index
                return i
            # Update the left sum by adding the current element
            left_sum += num
        # If no pivot index is found, return -1
