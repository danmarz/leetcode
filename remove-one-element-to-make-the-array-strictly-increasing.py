class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_strictly_increasing(arr):
            # Check if the array is strictly increasing
            for i in range(1, len(arr)):
                if arr[i - 1] >= arr[i]:
                    return False
            return True

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                # Try removing nums[i - 1] or nums[i]
                without_prev = nums[: i - 1] + nums[i:]
                without_curr = nums[:i] + nums[i + 1 :]
                return is_strictly_increasing(without_prev) or is_strictly_increasing(
                    without_curr
                )
        return True
