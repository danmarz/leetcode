class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of numbers from 0 to n.
        expected_sum = n * (n + 1) // 2
        # Calculate the actual sum of elements in nums.
        actual_sum = sum(nums)
        # Return the missing number.
        return expected_sum - actual_sum

        """
        # Brute force solution
        total = len(nums)
        for i in range(total):
            if i not in nums:
                return i
        return total
        """
