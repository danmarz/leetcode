class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_nums = 0
        sum_digits = 0

        for num in nums:
            sum_nums += num
            while num:
                sum_digits += num % 10
                num //= 10

        return abs(sum_nums - sum_digits)
