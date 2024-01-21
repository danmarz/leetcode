class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # Calculate the product of the last three elements
        max_product1 = nums[-1] * nums[-2] * nums[-3]

        # Calculate the product of the first two elements and the last element
        max_product2 = nums[0] * nums[1] * nums[-1]

        # Return the maximum of the two products
        return max(max_product1, max_product2)
