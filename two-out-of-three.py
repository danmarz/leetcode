class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        seen = {}

        for item in nums1:
            if item in nums2 or item in nums3:
                if item not in seen:
                    seen[item] = 1
                else:
                    seen[item] += 1
        for item in nums2:
            if item in nums1 or item in nums3:
                if item not in seen:
                    seen[item] = 1
                else:
                    seen[item] += 1
        for item in nums3:
            if item in nums1 or item in nums2:
                if item not in seen:
                    seen[item] = 1
                else:
                    seen[item] += 1

        return [key for key in seen.keys()]

        # Optimized approach using set operations
        # Convert arrays to sets to leverage set operations
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)

        # Use set union and intersection to find common elements
        result = (set1 & set2) | (set2 & set3) | (set3 & set1)

        # Convert the result back to a list and return
        return list(result)
