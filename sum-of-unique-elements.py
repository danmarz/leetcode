class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniques = set()
        doubles = set()

        for num in nums:
            if num not in uniques and num not in doubles:
                uniques.add(num)

            else:
                doubles.add(num)
                uniques.discard(num)

        return sum(uniques)
