class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Optimized approach for sorted arrays
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        result = []

        i, j = 0, 0  # Initialize pointers for both arrays

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

        """
        # Alternative using Counter import

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each number in both arrays.
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        result = []

        # Iterate through the numbers in nums1.
        for num in nums1:
            if num in counter2 and counter2[num] > 0:
                result.append(num)
                counter2[num] -= 1

        return result
        """
