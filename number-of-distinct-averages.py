class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # # Works, but isn't great efficiency-wise:
        # # O(n log n) + (n/2) * O(n) = O(n^2) in worst case due to pop(0)

        # nums = sorted(nums)
        # averages = set()
        
        # while nums:
        #     avg = (nums.pop(0) + nums.pop(-1)) / 2
        #     averages.add(avg)

        # return len(averages)

        # Reduces the overall complexity to that of the sorting step
        nums.sort()                           # O(n log n)
        averages = set()
        
        left, right = 0, len(nums) - 1
        while left < right:                  # O(n) total
            avg = (nums[left] + nums[right]) / 2
            averages.add(avg)
            left += 1
            right -= 1

        return len(averages)
