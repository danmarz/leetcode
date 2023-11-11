class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max = len(nums) + 1
        lst = [i for i in range(1, max)]

        nums = set(nums)
        lst = set(lst)

        ans = lst.difference(nums)
        return list(ans)
