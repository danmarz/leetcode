class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}  # Dictionary to store the last index of each element

        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True  # Found a duplicate within the specified range
            num_indices[num] = i  # Update the last index of the current element

        return False  # No duplicates found within the specified range
