class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # result = set(nums[0])
        # for num in nums:
        #     result &= set(num)
        # return list(sorted(result))

        # More elegant alternative: convert each subarray to a set and use set intersection
        common_elements = reduce(set.intersection, map(set, nums))

        # Return the sorted list of common elements
        return sorted(common_elements)
