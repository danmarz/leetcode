class Solution:
    def countElements(self, nums: List[int]) -> int:
        # nums_set = sorted(list(set(nums)))

        # if len(nums_set) < 3:
        #     return 0

        # count = 0

        # for i in range(1, len(nums_set) - 1):
        #     if nums_set[i + 1] > nums_set[i]:
        #         count += nums.count(nums_set[i])

        # return count

        # Optimized solution:
        # Find the smallest and largest elements
        smallest = min(nums)
        largest = max(nums)

        # Count elements strictly between the smallest and largest
        count = sum(1 for x in nums if smallest < x < largest)

        return count
