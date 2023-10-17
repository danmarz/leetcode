class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both arrays to Set instances to remove duplicates
        nums1 = set(nums1)
        nums2 = set(nums2)

        # Use set.intersection() with intersection operator (&) to find the common elements. list() optional.
        return nums1 & nums2

        """
        # Naive approach, iterating the first array and checking each value. O(n x m)
        ans = set()

        for num in nums1:
            if num in nums2:
                ans.add(num)

        return list(ans)
        """

        """
        # A better approach is to iterate over the smallest set checking the presence of each element in 
        # the larger set. Time complexity of this approach is O(n + m) in the average case.
        
        class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
        """
