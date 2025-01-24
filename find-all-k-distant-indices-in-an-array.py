class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for pos1, num in enumerate(nums):
            if num == key:
                for pos2, num in enumerate(nums):
                    if abs(pos1 - pos2) <= k:
                        result.add(pos2)
        return list(result)

        # # Optimized solution:
        # # Collect all indices of elements in nums that are equal to key
        # key_indices = [i for i, num in enumerate(nums) if num == key]

        # # Use a set to avoid duplicates
        # result = set()

        # for idx in key_indices:
        #     # Add all indices within k distance of the current key index
        #     start = max(0, idx - k)
        #     end = min(len(nums) - 1, idx + k)
        #     for i in range(start, end + 1):
        #         result.add(i)

        # # Convert the set to a sorted list and return
        # return sorted(result)
