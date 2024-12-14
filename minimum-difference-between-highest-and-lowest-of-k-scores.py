class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Edge case: If k is 1, the minimum difference is always 0
        if k == 1:
            return 0

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Initialize the minimum difference to a large value
        min_diff = float("inf")

        # Step 3: Slide a window of size k across the sorted array
        for i in range(len(nums) - k + 1):
            # Calculate the difference between the first and last element in the window
            diff = nums[i + k - 1] - nums[i]

            # Update the minimum difference
            min_diff = min(min_diff, diff)

        return min_diff
