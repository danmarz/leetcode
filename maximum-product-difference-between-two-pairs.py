class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nMin1, nMin2 = float("inf"), float("inf")  # Smallest and second smallest
        nMax1, nMax2 = float("-inf"), float("-inf")  # Largest and second largest

        for num in nums:
            # Update smallest values
            if num < nMin1:
                nMin2 = nMin1
                nMin1 = num
            elif num < nMin2:
                nMin2 = num

            # Update largest values
            if num > nMax1:
                nMax2 = nMax1
                nMax1 = num
            elif num > nMax2:
                nMax2 = num

        # Calculate the product difference
        return (nMax1 * nMax2) - (nMin1 * nMin2)

        # # More concise alternative, but less efficient for large lists O(n log n) vs O(n)
        # # Sort the array
        # nums.sort()
        # # Largest two numbers
        # max1, max2 = nums[-1], nums[-2]
        # # Smallest two numbers
        # min1, min2 = nums[0], nums[1]
        # # Calculate and return the product difference
        # return (max1 * max2) - (min1 * min2)
