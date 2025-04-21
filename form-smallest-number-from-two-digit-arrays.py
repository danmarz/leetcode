class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # set1 = set(nums1)
        # set2 = set(nums2)

        # intersection = set1 & set2

        # if not intersection:
        #     min1 = min(set1)
        #     min2 = min(set2)
        #     return min1 * 10 + min2 if min1 < min2 else min2 * 10 + min1
        # else:
        #     return min(intersection)

        # Optimal O(1) solution:
        # Boolean lookup tables for digits 1-9
        seen1 = [False] * 10
        seen2 = [False] * 10

        for n in nums1:
            seen1[n] = True
        for n in nums2:
            seen2[n] = True

        # Look for smallest common digit
        for d in range(1, 10):
            if seen1[d] and seen2[d]:
                return d

        # No common digit; find smallest cross-pair combination
        min1 = min(nums1)
        min2 = min(nums2)
        return min1 * 10 + min2 if min1 < min2 else min2 * 10 + min1
