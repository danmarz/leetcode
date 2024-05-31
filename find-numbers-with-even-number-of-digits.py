class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_nums = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                even_digit_nums += 1

        return even_digit_nums
