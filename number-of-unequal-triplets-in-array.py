class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i < n - 2:
            j = i + 1
            while j < n - 1:
                k = j + 1
                while k < n:
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans += 1
                    k += 1
                j += 1
            i += 1
        return ans
