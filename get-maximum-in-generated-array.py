class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # If n is 0, we return 0 immediately, because the array will only contain [0]
        if n == 0:
            return 0

        # Initialize the nums array with size n + 1 and set the first two values based on the problem statement.
        nums = [0] * (n + 1)
        nums[0], nums[1] = 0, 1

        # Initialize the maximum value as 1 because nums[1] = 1 and it's the first non-zero element.
        max_value = 1

        # Loop through from index 2 to n, building the array using the given rules.
        for i in range(2, n + 1):
            # For even indices, we use nums[2 * i] = nums[i]
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            # For odd indices, we use nums[2 * i + 1] = nums[i] + nums[i + 1]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            # Update the maximum value after calculating each new element.
            max_value = max(max_value, nums[i])

        # After constructing the nums array, return the maximum value found.
        return max_value
