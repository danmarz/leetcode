class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Convert nums to a set for O(1) lookup times
        num_set = set(nums)

        while original in num_set:
            original *= 2

        return original
