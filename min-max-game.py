class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # while len(nums) > 1:
        #     newLen = len(nums) // 2
        #     newNums = []
        #     for i in range(newLen):
        #         if i % 2 == 0:
        #             newNums.append(min(nums[2 * i], nums[2 * i + 1]))
        #         else:
        #             newNums.append(max(nums[2 * i], nums[2 * i + 1]))
        #     nums = newNums
        # return nums[0]

        while len(nums) > 1:
            nums = [
                (
                    min(nums[2 * i], nums[2 * i + 1])
                    if i % 2 == 0
                    else max(nums[2 * i], nums[2 * i + 1])
                )
                for i in range(len(nums) // 2)
            ]
        return nums[0]
