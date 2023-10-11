class NumArray:
    # Pre-computed list of sums.
    # Optimized for performing multiple range-sum queries with a time complexity of O(1):

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]  # Initialize a list to store the prefix sum.
        curr_sum = 0

        # Calculate and store the prefix sum for each element in nums.
        for num in nums:
            curr_sum += num
            self.prefix_sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        # To calculate the sum of elements between left and right inclusive,
        # you can use the prefix sum technique:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

    """ Sub-optimal solution below:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for n in range(i, j + 1):
            sum += self.nums[n]
        return sum
    """


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
