class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()

        # Initialize the minimum score with the score of the original array
        min_score = nums[-1] - nums[0]

        # Try adjusting the first and last elements
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Adjust the current range by k
                min_val = nums[i] + k
                max_val = nums[j] - k

                # Recalculate the score after adjustment
                min_score = min(min_score, max_val - min_val)

        return max(0, min_score)  # Return 0 if min_score is negative
