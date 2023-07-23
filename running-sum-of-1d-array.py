class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = []
        for i  in range(len(nums)):
            rs.append( sum(nums[:i + 1]) )
        return rs
