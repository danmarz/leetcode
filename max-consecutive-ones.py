class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0  # Initialize the maximum consecutive count of 1's
        current_ones = 0  # Initialize the current consecutive count of 1's

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)  # Update max_ones if needed
            else:
                current_ones = 0  # Reset current count if the current number is 0

        return max_ones
