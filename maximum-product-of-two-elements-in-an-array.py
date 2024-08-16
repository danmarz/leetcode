class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the array in descending order so that the largest numbers are at the front
        nums.sort(reverse=True)

        # Take the two largest elements, which are now at indices 0 and 1
        max1 = nums[0]
        max2 = nums[1]

        # Compute and return the product (max1 - 1) * (max2 - 1)
        return (max1 - 1) * (max2 - 1)
