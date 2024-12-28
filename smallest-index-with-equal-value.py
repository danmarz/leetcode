class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

        # # Pythonic approach using next():
        # return next((i for i, num in enumerate(nums) if i % 10 == num), -1)
