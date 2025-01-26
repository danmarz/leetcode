class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Step 1: Remove adjacent duplicates using a list comprehension
        deduplicated_nums = [
            nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]
        ]

        # Step 2: Count hills and valleys
        result = sum(
            1
            for i in range(1, len(deduplicated_nums) - 1)
            if (
                deduplicated_nums[i] > deduplicated_nums[i - 1]
                and deduplicated_nums[i] > deduplicated_nums[i + 1]
            )
            or (
                deduplicated_nums[i] < deduplicated_nums[i - 1]
                and deduplicated_nums[i] < deduplicated_nums[i + 1]
            )
        )

        return result
