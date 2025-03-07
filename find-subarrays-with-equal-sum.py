class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = set()

        for i in range(len(nums) - 1):
            pair_sum = nums[i] + nums[i + 1]
            if pair_sum in seen_sums:
                return True
            seen_sums.add(pair_sum)

        return False
