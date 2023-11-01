class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float("-inf")
        unique_nums = set(nums)

        for num in unique_nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num

        return third_max if len(unique_nums) >= 3 else first_max

        """ # Python sorted() works in O(n log n) space
        nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]
        """
