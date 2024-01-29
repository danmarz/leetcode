class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Edge case: empty array
        if not nums:
            return 0

        # Initialize variables to store current and maximum lengths
        current_length = 1
        max_length = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is greater than the previous one
            if nums[i] > nums[i - 1]:
                # If yes, increment the current length
                current_length += 1
            else:
                # If not, update the maximum length and reset the current length
                max_length = max(max_length, current_length)
                current_length = 1

        # Update the maximum length after the loop
        max_length = max(max_length, current_length)

        return max_length
