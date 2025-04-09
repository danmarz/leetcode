class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ns = str(n)
            for c in ns:
                ans.append(int(c))
        return ans
