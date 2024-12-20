class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # # O(n^2)
        # fast = 1
        # max_diff = -1
        # while fast < len(nums):
        #     for num in nums[:fast]:
        #         if nums[fast] > num:
        #             max_diff = max(nums[fast] - num, max_diff)
        #     fast += 1
        # return max_diff

        # O(n) approach, optimized time complexity
        n = len(nums)
        min_so_far = float("inf")  # Initialize with infinity
        max_diff = -1

        for num in nums:
            if num > min_so_far:  # Calculate difference only if the condition is met
                max_diff = max(max_diff, num - min_so_far)
            min_so_far = min(min_so_far, num)  # Update the smallest value seen so far

        return max_diff
