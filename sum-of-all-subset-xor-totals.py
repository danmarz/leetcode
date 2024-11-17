class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Be cooler than most:
        return (reduce(lambda x, y: x | y, nums)) << (len(nums) - 1)

        # # Optimal approach, using bit manipulation
        # n = len(nums)
        # total = 0

        # for i in range(1 << n):  # Iterate through all subsets
        #     subset_xor = 0
        #     for j in range(n):
        #         if i & (1 << j):  # Check if j-th element is in the subset
        #             subset_xor ^= nums[j]
        #     total += subset_xor

        # return total

        # # Using combinations() is an easy solution to generating all possible subsets of nums
        # n = len(nums)
        # total = 0

        # # Generate all subsets
        # for i in range(n + 1):  # i is the size of the subset
        #     for subset in combinations(nums, i):
        #         # Compute XOR total of the subset
        #         xor_total = 0
        #         for num in subset:
        #             xor_total ^= num
        #         total += xor_total

        # return total

        # Bruteforce approach, slower
        # def generate_subsets(array):
        #     def backtrack(index, current):
        #         # Base case: if we've considered all elements
        #         if index == len(array):
        #             subsets.append(current[:])  # Add a copy of the current subset
        #             return

        #         # Recursive case: Exclude the current element
        #         backtrack(index + 1, current)

        #         # Recursive case: Include the current element
        #         current.append(array[index])  # Add the element to the current subset
        #         backtrack(index + 1, current)  # Recurse
        #         current.pop()  # Backtrack: remove the element added above

        #     subsets = []
        #     backtrack(0, [])  # Start recursion with index 0 and an empty subset
        #     return subsets

        # all_subsets = generate_subsets(nums)
        # sum_xor = 0

        # # print(all_subsets)
        # for subset in all_subsets:
        #     result = 0
        #     for i in subset:
        #         result ^= i
        #     sum_xor += result

        # return sum_xor
