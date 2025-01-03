class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # return [pos for pos,num in enumerate(sorted(nums)) if num == target]

        # Optimized, O(n) approach
        count_less = 0
        target_count = 0

        for num in nums:
            if num == target:
                target_count += 1
            elif num < target:
                count_less += 1
        if count == 0:
            return []

        return list(range(count_less, count_less + target_count))
