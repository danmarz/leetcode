class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)

        if n % 2 == 1:
            concat = nums[n // 2]
        else:
            concat = 0

        i = 0
        while i < n // 2:
            num = int(str(nums[i]) + str(nums[-i - 1]))
            concat += num
            i += 1

        return concat
