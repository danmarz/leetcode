class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_n1 = set(nums1)
        set_n2 = set(nums2)

        common = set_n1 & set_n2

        if not common:
            return -1
        else:
            return min(common)
