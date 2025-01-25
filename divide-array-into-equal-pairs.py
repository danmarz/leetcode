class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num in count:
            if count.get(num) % 2 != 0:
                return False

        return True
