class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []

        # set(nums1) - set(nums2) is syntactic sugar for set(nums1).difference(set(nums2))
        answer.append(list(set(nums1) - set(nums2)))
        answer.append(list(set(nums2) - set(nums1)))

        return answer
