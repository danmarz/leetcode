class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # If the middle element is less than the target, search the right half
            elif nums[mid] < target:
                left = mid + 1

            # If the middle element is greater than the target, search the left half
            else:
                right = mid - 1

        # If target is not found, return -1
        return -1
