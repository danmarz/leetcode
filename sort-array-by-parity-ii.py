class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        ans = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])

        return ans
