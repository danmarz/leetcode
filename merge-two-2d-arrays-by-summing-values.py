class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        merged = dict(nums1)  # Initialize dict from nums1

        for n, val in nums2:  # Unpack directly
            if n in merged:  # No need for .keys()
                merged[n] += val
            else:
                merged[n] = val

        # Convert to list of lists and sort by id
        return [list(item) for item in sorted(merged.items())]
