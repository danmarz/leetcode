class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        num_set = set(nums)

        max_k = -1  # default if no such k is found
        for val in nums:
            # If val is positive and its negative counterpart is in the set
            if val > 0 and -val in num_set:
                max_k = max(max_k, val)

        return max_k
