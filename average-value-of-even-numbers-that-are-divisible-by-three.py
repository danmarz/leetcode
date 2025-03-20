class Solution:
    def averageValue(self, nums: List[int]) -> int:
        items = 0
        sum_of_items = 0

        for num in nums:
            if num % 6 == 0:
                sum_of_items += num
                items += 1
        
        return int(sum_of_items / items) if items >= 1 else items
