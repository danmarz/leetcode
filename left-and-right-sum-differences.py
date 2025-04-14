class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # leftSum = 0
        # rightSum = sum(nums[1:])
        # ans = [abs(leftSum - rightSum)]

        # for i in range(len(nums) - 1):
        #     leftSum += nums[i]
        #     rightSum -= nums[i + 1]
        #     ans.append(abs(leftSum - rightSum))

        # return ans

        # Optimized solution (still O(n), but avoids slicing)
        total = sum(nums)  # Total sum of array
        leftSum = 0
        ans = []

        for num in nums:
            rightSum = total - leftSum - num  # Subtract left + current to get right
            ans.append(abs(leftSum - rightSum))
            leftSum += num

        return ans
